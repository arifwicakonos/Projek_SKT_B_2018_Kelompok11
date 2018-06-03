//Send.ino
 
#include<SPI.h>
#include<RF24.h>

int smokeA0 = A5;
// Your threshold value
int sensorThres = 400;
 
// ce, csn pins
RF24 radio(9, 10);
const uint64_t wadd = 0xF0F0F0F0C5LL;
const uint64_t radd = 0xF0F0F0F0A4LL; 

void setup(void){
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(wadd);
  radio.openReadingPipe(1, radd);
  radio.enableDynamicPayloads();
  radio.stopListening();
  radio.powerUp();

  Serial.begin(9600);
  pinMode(smokeA0, INPUT);
 
}
 
void loop(void){

  int analogSensor = analogRead(smokeA0);

  Serial.print("Pin A5: ");
  Serial.println(analogSensor);
  // Checks if it has reached the threshold value
  if (analogSensor > sensorThres)
  {
    Serial.println ("ada asap");
    const char text[] = "1";
    radio.write(&text, sizeof(text));
  }
  else
  {
    Serial.println("gak ada asap");
    const char text[] = "0";
    radio.write(&text, sizeof(text));
  }
  
  delay(1000);
 
}
