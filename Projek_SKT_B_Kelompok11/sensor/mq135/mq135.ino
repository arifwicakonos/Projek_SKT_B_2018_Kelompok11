#include<SPI.h>
#include<RF24.h>
#include<nRF24L01.h>

RF24 radio(9, 10);
const uint64_t wadd = 0xF0F0F0F0C4LL;
const uint64_t radd = 0xF0F0F0F0A3LL;

int sensorValue;
int digitalValue;
String str;
char cstr[16];
void setup()
{
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(wadd);
  radio.openReadingPipe(1, radd);
  radio.enableDynamicPayloads();
  radio.stopListening();
  radio.powerUp();
  
  Serial.begin(9600);      // sets the serial port to 9600
  pinMode( 0, INPUT);
}

void loop()
{
  sensorValue = analogRead(0);       // read analog input pin 0
  Serial.println(sensorValue, DEC);  // prints the value read
  str = String(sensorValue);
  str.toCharArray(cstr, 16);
  radio.write(&cstr, sizeof(cstr));  
  delay(500);                        // wait 100ms for next reading
}
