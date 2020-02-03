#include <SPI.h>
const int cs = 9;
unsigned int test = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
SPI.begin();
pinMode(cs, OUTPUT);

}
//MISO is pin 19
//MOSI is pin 23 (not required)
//SCK is pin 18

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(cs, LOW);
SPI.beginTransaction(SPISettings(125000, MSBFIRST, SPI_MODE1));
test = SPI.transfer16(0x00);
test = test& 0b111111111111;
test >> 1;
Serial.println(test);
digitalWrite(cs, HIGH);
SPI.endTransaction();
delay(10);
}
