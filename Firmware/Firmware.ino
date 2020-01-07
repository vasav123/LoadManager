#include <Wire.h>
#include <SPI.h>

#include <WiFi.h>
#include "PubSubClient.h"
#include "ArduinoJson.h"

#include <SparkFunLSM9DS1.h>


/* Defs for network connfiguration and MQTT Broker */
const char* ssid     = "Vasav-Computer";
const char* password = "6fQBxWeq";
const char* mqtt_server = "10.42.0.1";
const char* nodeId = "123123123";
int port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

LSM9DS1 imu;

#define PRINT_CALCULATED
#define PRINT_SPEED 250 // 250 ms between prints
static unsigned long lastPrint = 0; // Keep track of print time
const char* publishNode = "loadmanager";

// http://www.ngdc.noaa.gov/geomag-web/#declination
#define DECLINATION 9.92 // Declination (degrees) in Hamilton Ontario.

//Function definitions
void printGyro();
void printAccel();
void printMag();
void printAttitude(float ax, float ay, float az, float mx, float my, float mz, float *heading, float *pitch, float *roll);

/* Setup the WiFi Connection when required */
void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);
  int timeout=0;
  while (WiFi.status() != WL_CONNECTED && timeout++<100) {
    delay(500);
    Serial.print(".");
  }
  if(timeout<100){
    randomSeed(micros());
  
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
  }else{
    Serial.println("wifi not connected!");
  }
}

/* reconnection */
void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    String clientId = "SensorNode-";
    clientId += nodeId;
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup()
{
  Serial.begin(115200);

  setup_wifi();
  client.setServer(mqtt_server, port);

  Wire.begin();

  if (imu.begin() == false) // with no arguments, this uses default addresses (AG:0x6B, M:0x1E) and i2c port (Wire).
  {
    Serial.println("Failed to communicate with LSM9DS1.");
    Serial.println("Double-check wiring.");
    Serial.println("Default settings in this sketch will " \
                   "work for an out of the box LSM9DS1 " \
                   "Breakout, but may need to be modified " \
                   "if the board jumpers are.");
    while (1);
  }
}

void loop()
{
  if (WiFi.status() == WL_CONNECTED){
    if (!client.connected()) {
      reconnect();
    }
    client.loop();
    
    long now = millis();
//    Serial.print("Publish message: ");
//    Serial.println(msg);
    client.publish(publishNode, "hello world");
//  WiFi.disconnect();
  }else{
    Serial.println("wifi not connected going to restart in 5 mins!");
  }
  if ( imu.gyroAvailable() )
  {
    imu.readGyro();
  }
  if ( imu.accelAvailable() )
  {
    imu.readAccel();
  }
  if ( imu.magAvailable() )
  {
    imu.readMag();
  }

  if ((lastPrint + PRINT_SPEED) < millis())
  {
    float heading, pitch, roll;
    printGyro();  // Print "G: gx, gy, gz"
    printAccel(); // Print "A: ax, ay, az"
    printMag();   // Print "M: mx, my, mz"
    printAttitude(imu.ax, imu.ay, imu.az,
                  -imu.my, -imu.mx, imu.mz,
                   &heading, &pitch, &roll);

    
    lastPrint = millis(); // Update lastPrint time
  }
}

void printGyro()
{
  // Now we can use the gx, gy, and gz variables as we please.
  // Either print them as raw ADC values, or calculated in DPS.
  Serial.print("G: ");
#ifdef PRINT_CALCULATED
  // If you want to print calculated values, you can use the
  // calcGyro helper function to convert a raw ADC value to
  // DPS. Give the function the value that you want to convert.
  Serial.print(imu.calcGyro(imu.gx), 2);
  Serial.print(", ");
  Serial.print(imu.calcGyro(imu.gy), 2);
  Serial.print(", ");
  Serial.print(imu.calcGyro(imu.gz), 2);
  Serial.println(" deg/s");
#elif defined PRINT_RAW
  Serial.print(imu.gx);
  Serial.print(", ");
  Serial.print(imu.gy);
  Serial.print(", ");
  Serial.println(imu.gz);
#endif
}

void printAccel()
{
  // Now we can use the ax, ay, and az variables as we please.
  // Either print them as raw ADC values, or calculated in g's.
  Serial.print("A: ");
#ifdef PRINT_CALCULATED
  // If you want to print calculated values, you can use the
  // calcAccel helper function to convert a raw ADC value to
  // g's. Give the function the value that you want to convert.
  Serial.print(imu.calcAccel(imu.ax), 2);
  Serial.print(", ");
  Serial.print(imu.calcAccel(imu.ay), 2);
  Serial.print(", ");
  Serial.print(imu.calcAccel(imu.az), 2);
  Serial.println(" g");
#elif defined PRINT_RAW
  Serial.print(imu.ax);
  Serial.print(", ");
  Serial.print(imu.ay);
  Serial.print(", ");
  Serial.println(imu.az);
#endif

}

void printMag()
{
  // Now we can use the mx, my, and mz variables as we please.
  // Either print them as raw ADC values, or calculated in Gauss.
  Serial.print("M: ");
#ifdef PRINT_CALCULATED
  // If you want to print calculated values, you can use the
  // calcMag helper function to convert a raw ADC value to
  // Gauss. Give the function the value that you want to convert.
  Serial.print(imu.calcMag(imu.mx), 2);
  Serial.print(", ");
  Serial.print(imu.calcMag(imu.my), 2);
  Serial.print(", ");
  Serial.print(imu.calcMag(imu.mz), 2);
  Serial.println(" gauss");
#elif defined PRINT_RAW
  Serial.print(imu.mx);
  Serial.print(", ");
  Serial.print(imu.my);
  Serial.print(", ");
  Serial.println(imu.mz);
#endif
}

// Calculate pitch, roll, and heading.
// Pitch/roll calculations take from this app note:
// http://cache.freescale.com/files/sensors/doc/app_note/AN3461.pdf?fpsp=1
// Heading calculations taken from this app note:
// http://www51.honeywell.com/aero/common/documents/myaerospacecatalog-documents/Defense_Brochures-documents/Magnetic__Literature_Application_notes-documents/AN203_Compass_Heading_Using_Magnetometers.pdf
void printAttitude(float ax, float ay, float az, float mx, float my, float mz, float *heading, float *pitch, float *roll)
{
  *roll = atan2(ay, az);
  *pitch = atan2(-ax, sqrt(ay * ay + az * az));

//  float heading;
  if (my == 0)
    *heading = (mx < 0) ? PI : 0;
  else
    *heading = atan2(mx, my);

  *heading -= DECLINATION * PI / 180;

  if (*heading > PI) *heading -= (2 * PI);
  else if (*heading < -PI) *heading += (2 * PI);

  // Convert everything from radians to degrees:
  *heading *= 180.0 / PI;
  *pitch *= 180.0 / PI;
  *roll  *= 180.0 / PI;
}
