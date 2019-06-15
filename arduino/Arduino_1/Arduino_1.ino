
#include <Wire.h>

#define SLAVE_ADDRESS 0x12


#include "DHT.h"
#define DHTPIN 11 // What pin we're connected to - A quelle broche nous sommes connectés
#define DHTTYPE DHT22 // DHT 22  (AM2302)


#define FIRSTLEDPIN 2
#define NBLED 5

#define CMDBUFSIZE 10
char command[CMDBUFSIZE];

// Initialize DHT sensor for normal 16mhz Arduino - Initialiser le capteur DHT pour l'Arduino 16mhz normal
DHT dht(DHTPIN, DHTTYPE);

// Data block for the raspberry pi - Block de donnée pour le raspberry pi
struct STATUS_INFO  { 
  float humidity;
  float temperature;
  byte leds[NBLED];
  };

STATUS_INFO status_info;

void setup() {
  Serial.begin(9600);
  
  Serial.println("DHT22 init");
  dht.begin();

  // Activate leds - Active les leds
  for(int led = 0; led < NBLED; led++) {
    pinMode(FIRSTLEDPIN + led, OUTPUT);
    status_info.leds[led] = 0;
  }

  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.print("Arduino Started i2c port ");
  Serial.println(SLAVE_ADDRESS);

}

void setLight(int led,bool lightOn) {
  if (lightOn) {
    digitalWrite(FIRSTLEDPIN + led, HIGH);
    status_info.leds[led] = 1;
  } else {
    digitalWrite(FIRSTLEDPIN + led, LOW);
    status_info.leds[led] = 0;
  }
}

void loop() {
  // Store the humidity and the temperature so it can be sent when requested
  // Stocker l'humidité et la température pour pouvoir l'envoyer sur demande
  status_info.humidity = dht.readHumidity();
  status_info.temperature = dht.readTemperature();
  delay(100);
}

void receiveData(int byteCount) {
    int i = 0;
    while(Wire.available()) {
        command[i] = Wire.read();
        if (i < CMDBUFSIZE && i < byteCount) i++;
    }
    
    Serial.print("Command received:");
    Serial.println(command);
    
    if (command[0] == 'L') {
        // Set the light - Régle la lumière
        int light = int(command[1]-'0');
        Serial.print("setlight:");
        Serial.print(light);
        Serial.println(command[2]);
        
        if (light >= 0 && light < 5) {
          if (command[2] == 'O') {
              setLight(light, true);
          } else if (command[2] == 'F') {
              setLight(light, false);
        }
        
    } else {
        Serial.println(command[0]);
    }
}


void sendData() {
  // Send humidity and temperature and leds data
  // Envoyer les données d'humidité et de température et les leds
  Wire.write((byte*)(&status_info),sizeof(status_info));  
}
