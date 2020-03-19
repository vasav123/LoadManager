#include <Wire.h>
#include <SPI.h>
#include <WiFi.h>
#include "PubSubClient.h"
#include "ArduinoJson.h"

#include <SparkFunLSM9DS1.h>

#define COMPUTER 1 // 0 for Michael and 1 for Vasav- home network 2 -Vasav Hotspot
#if COMPUTER == 0
  #define S_SID  "Michael-Computer"
  #define SERVER "192.168.137.1"
  #define PASSWORD "6fQBxWeq"
#elif COMPUTER == 1
  #define S_SID "VIRGIN247"
  #define SERVER "192.168.2.32"
  #define PASSWORD "D47E4A67"
#else
  #define S_SID "Vasav-Computer"
  #define SERVER "10.42.0.1"
  #define PASSWORD "6fQBxWeq"
#endif
const char* ssid     = S_SID;//"Michael-Computer" -- "Vasav-Computer"
const char* password = PASSWORD;//Same password for both
const char* mqtt_server = SERVER;//Vasav- "10.42.0.1", Michael, 192.168.137.1
const char* nodeId = "123123123";
int port = 1883;
int packet_num = 0;
int cs_1 = 9;
int cs_2 = 10; // need to change this
WiFiClient espClient;
PubSubClient client(espClient);

LSM9DS1 imu;
LSM9DS1 imu2;


#define PRINT_CALCULATED
#define PRINT_SPEED 5 // 250 ms between prints
int count = 0;
static unsigned long lastPrint = 0; // Keep track of print time
const char* publishNode = "loadmanager";

StaticJsonDocument<3000> packet;
char msg[3000];

float temp_array[4];

// http://www.ngdc.noaa.gov/geomag-web/#declination
#define DECLINATION 9.92 // Declination (degrees) in Hamilton Ontario.

void printAttitude(float ax, float ay, float az, float mx, float my, float mz, float *heading, float *pitch, float *roll);
float getMagnitude(float x, float y, float z);
unsigned int readFSR(int fsr);
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
      delay(5);
    }
  }
}

void setup()
{
  Serial.begin(115200);
  
  packet.createNestedArray("ax_t");
  copyArray(temp_array, 4, packet["ax_t"]);
  packet.createNestedArray("ay_t");
  copyArray(temp_array, 4, packet["ay_t"]);
  packet.createNestedArray("az_t");
  copyArray(temp_array, 4, packet["az_t"]);
  
  packet.createNestedArray("ax_b");
  copyArray(temp_array, 4, packet["ax_b"]);
  packet.createNestedArray("ay_b");
  copyArray(temp_array, 4, packet["ay_b"]);
  packet.createNestedArray("az_b");
  copyArray(temp_array, 4, packet["az_b"]);
   
  packet.createNestedArray("gx_t");
  copyArray(temp_array, 4, packet["gx_t"]);
  packet.createNestedArray("gy_t");
  copyArray(temp_array, 4, packet["gy_t"]);
  packet.createNestedArray("gz_t");
  copyArray(temp_array, 4, packet["gz_t"]);

  packet.createNestedArray("gx_b");
  copyArray(temp_array, 4, packet["gx_b"]);
  packet.createNestedArray("gy_b");
  copyArray(temp_array, 4, packet["gy_b"]);
  packet.createNestedArray("gz_b");
  copyArray(temp_array, 4, packet["gz_b"]);

  packet.createNestedArray("my_t");
  copyArray(temp_array, 4, packet["mx_t"]);
  packet.createNestedArray("my_t");
  copyArray(temp_array, 4, packet["my_t"]);
  packet.createNestedArray("mz_t");
  copyArray(temp_array, 4, packet["mz_t"]);

  packet.createNestedArray("my_b");
  copyArray(temp_array, 4, packet["mx_b"]);
  packet.createNestedArray("my_b");
  copyArray(temp_array, 4, packet["my_b"]);
  packet.createNestedArray("mz_b");
  copyArray(temp_array, 4, packet["mz_b"]);

  packet.createNestedArray("fq");
  copyArray(temp_array, 4, packet["fq"]);
  packet.createNestedArray("fh");
  copyArray(temp_array, 4, packet["fh"]);

  setup_wifi();
  client.setServer(mqtt_server, port);
  Wire.begin();               //21 clk 22 data
  Wire1.begin(13,14,100000); //13 clk 14 data
  SPI.begin();
  pinMode(cs_1, OUTPUT);
  pinMode(cs_2, OUTPUT);

  if (imu.begin() == false) // with no arguments, this uses default addresses (AG:0x6B, M:0x1E) and i2c port (Wire).
  {
    Serial.println("Failed to communicate with LSM9DS1.");
    Serial.println("Double-check wiring.");
    Serial.println("Default settings in this sketch will " \
                   "work for an out of the box LSM9DS1 " \
                   "Breakout, but may need to be modified " \
                   "if the board jumpers are.");
    while (1);
  }else{
    Serial.println("IMU1 connected!");
  }
 if (imu2.begin( LSM9DS1_AG_ADDR(1), LSM9DS1_M_ADDR(1), Wire1) == false) // with no arguments, this uses default addresses (AG:0x6B, M:0x1E) and i2c port (Wire).
 {
   Serial.println("Failed to communicate with LSM9DS1.");
   Serial.println("Double-check wiring.");
   Serial.println("Default settings in this sketch will " \
                  "work for an out of the box LSM9DS1 " \
                  "Breakout, but may need to be modified " \
                  "if the board jumpers are.");
   while (1);
 }else{
   Serial.println("IMU2 connected!");
 }
  imu.setAccelScale(16);
  imu2.setAccelScale(16);
  imu.setGyroScale(500);
  imu2.setGyroScale(500);
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
 if ( imu2.gyroAvailable() )
 {
   imu2.readGyro();
 }
 if ( imu2.accelAvailable() )
 {
   imu2.readAccel();
 }
 if ( imu2.magAvailable() )
 {
   imu2.readMag();
 }
  if ((lastPrint + PRINT_SPEED) < millis())
  {
  
    packet["ax_t"][count] = imu.calcAccel(imu.ax);
    packet["ay_t"][count] = imu.calcAccel(imu.ay);
    packet["az_t"][count] = imu.calcAccel(imu.az);
    packet["ax_b"][count] = imu.calcAccel(imu2.ax);
    packet["ay_b"][count] = imu.calcAccel(imu2.ay);
    packet["az_b"][count] = imu.calcAccel(imu2.az);
    packet["gx_t"][count] = imu.calcGyro(imu.gx);
    packet["gy_t"][count] = imu.calcGyro(imu.gy);
    packet["gz_t"][count] = imu.calcGyro(imu.gz);
    packet["gx_b"][count] = imu.calcGyro(imu2.gx);
    packet["gy_b"][count] = imu.calcGyro(imu2.gy);
    packet["gz_b"][count] = imu.calcGyro(imu2.gz);
    packet["mx_t"][count] = imu.calcMag(imu.mx);
    packet["my_t"][count] = imu.calcMag(imu.my);
    packet["mz_t"][count] = imu.calcMag(imu.mz);
    packet["mx_b"][count] = imu.calcMag(imu2.mx);
    packet["my_b"][count] = imu.calcMag(imu2.my);
    packet["mz_b"][count] = imu.calcMag(imu2.mz);
    packet["fq"][count] = readFSR(0);
    packet["fh"][count] = readFSR(1);
    count++;
    serializeJson(packet, msg);
    lastPrint = millis(); // Update lastPrint time
    
//    Serial.println(msg);
    
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

unsigned int readFSR(int fsr){
  if (fsr == 0){
    digitalWrite(cs_1, LOW);
  }else{
    digitalWrite(cs_2, LOW);
  }
  SPI.beginTransaction(SPISettings(125000, MSBFIRST, SPI_MODE1));
  unsigned int fsr_value = 0;
  fsr_value = SPI.transfer16(0x00);
  fsr_value = fsr_value& 0b111111111111;
  fsr_value >> 1;

  if (fsr == 0){
    digitalWrite(cs_1, HIGH);
  }else{
    digitalWrite(cs_2, HIGH);
  }
  SPI.endTransaction();
  return fsr_value;
}
