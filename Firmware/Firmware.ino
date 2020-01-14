#include <dummy.h>

#include <Wire.h>
#include <SPI.h>
#include <WiFi.h>
#include "PubSubClient.h"
#include "ArduinoJson.h"

#include <SparkFunLSM9DS1.h>

const char* ssid     = "Michael-Computer";//"Michael-Computer" -- "Vasav-Computer"
const char* password = "6fQBxWeq";//Same password for both
const char* mqtt_server = "192.168.137.1";//Vasav- "10.42.0.1", Michael, 192.168.137.1
const char* nodeId = "123123123";
int port = 1883;
int packet_num = 0;

WiFiClient espClient;
PubSubClient client(espClient);

LSM9DS1 imu;

#define PRINT_CALCULATED
#define PRINT_SPEED 250 // 250 ms between prints
int count = 0;
static unsigned long lastPrint = 0; // Keep track of print time
const char* publishNode = "loadmanager";

StaticJsonDocument<1000> packet;
char msg[2000];

float temp_array[4];

// http://www.ngdc.noaa.gov/geomag-web/#declination
#define DECLINATION 9.92 // Declination (degrees) in Hamilton Ontario.

void printAttitude(float ax, float ay, float az, float mx, float my, float mz, float *heading, float *pitch, float *roll);
float getMagnitude(float x, float y, float z);

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
  packet.createNestedArray("accel_top");
  copyArray(temp_array, 4, packet["accel_top"]);
  packet.createNestedArray("accel_bot");
  copyArray(temp_array, 4, packet["accel_bot"]);
  packet.createNestedArray("fsr_quad");
  copyArray(temp_array, 4, packet["fsr_quad"]);
  packet.createNestedArray("fsr_ham");
  copyArray(temp_array, 4, packet["fsr_ham"]);
  packet.createNestedArray("yaw_top");
  copyArray(temp_array, 4, packet["yaw_top"]);
  packet.createNestedArray("pitch_top");
  copyArray(temp_array, 4, packet["pitch_top"]);
  packet.createNestedArray("roll_top");
  copyArray(temp_array, 4, packet["roll_top"]);
  packet.createNestedArray("yaw_bot");
  copyArray(temp_array, 4, packet["yaw_bot"]);
  packet.createNestedArray("pitch_bot");
  copyArray(temp_array, 4, packet["pitch_bot"]);
  packet.createNestedArray("roll_bot");
  copyArray(temp_array, 4, packet["roll_bot"]);

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
    float heading =0 , pitch = 0 , roll = 0;
    calcAttitude(imu.ax, imu.ay, imu.az,
                  -imu.my, -imu.mx, imu.mz,
                   &heading, &pitch, &roll);
   
    packet["pitch_top"][count] = pitch;
    packet["pitch_bot"][count] = 0;
    packet["yaw_top"][count] = heading;
    packet["yaw_bot"][count] = 0;
    packet["roll_top"][count] = roll;
    packet["roll_bot"][count] = 0;
    packet["accel_top"][count] = getMagnitude(imu.calcAccel(imu.ax), imu.calcAccel(imu.ay), imu.calcAccel(imu.az));
    packet["accel_bot"][count] = 0;
    packet["fsr_quad"][count] = analogRead(33);
    packet["fsr_ham"][count] = 0;
    count++;
    serializeJson(packet, msg);
    lastPrint = millis(); // Update lastPrint time
    
//    Serial.println(pitch);
    
    if (count == 4){
        packet_num++;
        packet["packet_num"] = packet_num;
        count = 0;
        if (WiFi.status() == WL_CONNECTED){
          if (!client.connected()) {
            reconnect();
          }
          client.loop();
          long now = millis();
          client.publish(publishNode, msg);
          packet["size"] = 4;
      }else{
        Serial.println("wifi not connected");
      }
    }
  }
}

float getMagnitude(float x, float y, float z)
{
  return sqrt(pow(x,2) + pow(y,2) + pow(z,2));
}
void calcAttitude(float ax, float ay, float az, float mx, float my, float mz, float *heading, float *pitch, float *roll)
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
