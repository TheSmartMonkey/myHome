
#include <Wire.h>

#define SLAVE_ADDRESS 0x12


#include "DHT.h"
#define DHTPIN 11     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)


#define FIRSTLED 2
#define LASTLED 6

#define CMDBUFSIZE 10
char command[CMDBUFSIZE];

// Initialize DHT sensor for normal 16mhz Arduino
DHT dht(DHTPIN, DHTTYPE);

struct DHT_INFO  { 
  float humidity;
  float temperature;
  };

DHT_INFO dht_info;

void setup() {
  Serial.begin(9600); 
  
  Serial.println("DHT22 init");
  dht.begin();

  for(int led=FIRSTLED;led<=LASTLED;led++) {
    pinMode(led, OUTPUT);
  }

  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.print("Arduino Started i2c port ");
  Serial.println(SLAVE_ADDRESS);

}

void setLight(int led,bool lightOn) {
  if (lightOn) {
    digitalWrite(led+FIRSTLED, HIGH);
    }
  else {
    digitalWrite(led+FIRSTLED, LOW);
    }
 
}

void loop() {
  // we store the humidity and the temperature so it can be sent when requested
  dht_info.humidity = dht.readHumidity();
  dht_info.temperature = dht.readTemperature();
  delay(100);
}

void receiveData(int byteCount){
    int i=0;
    while(Wire.available()) {
        command[i] = Wire.read();
        if (i<CMDBUFSIZE && i<byteCount) i++;
    }    
    Serial.print("Command received:");
    Serial.println(command);
    if (command[0]=='L') {
        // set the light
        int light=int(command[1]-'0');
        Serial.print("setlight:");
        Serial.print(light);
        Serial.println(command[2]);
        if (light>=0 && light<5) {
          if (command[2]=='O')
              setLight(light,true);
          else if (command[2]=='F')
              setLight(light,false);
        }
      else
        Serial.println(command[0]);
    }
    
}


void sendData() {
  // send humidity and temperature data 
  byte buff[sizeof(DHT_INFO)];
  memcpy(buff,&dht_info,sizeof(dht_info));
  Wire.write(buff,sizeof(dht_info));  
}
