/*
 * -----------------------------------------------------------------------------------------
 *             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
 *             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
 * Signal      Pin          Pin           Pin       Pin        Pin              Pin
 * -----------------------------------------------------------------------------------------
 * RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
 * SPI SS      SDA(SS)      10            53        D10        10               10
 * SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
 * SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
 * SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
*/

#include <Wire.h>
#define SLAVE_ADDRESS 0x13

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9           // Configurable, see typical pin layout above
#define SS_PIN          10          // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance


#define DOORSERVO 5     // PIN Where the door servo is connected
#define OPEN_ANGLE 130  // set this value for the door to fully open
#define CLOSED_ANGLE 30 // set this value for the door to fully close


#include <Servo.h>

// Servo control
Servo doorservo;  // create servo object to control the door servo

#define CMDBUFSIZE 10
char command[CMDBUFSIZE];

struct STATUS_INFO  { 
  byte dooropen = false;
  };

long lastActionTime;

STATUS_INFO status_info;

void setup() {
  // Initialize serial communications with the PC
  // Initialiser les communications série avec le PC
  Serial.begin(9600); 
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.print("Arduino Started i2c port ");
  Serial.println(SLAVE_ADDRESS);

  SPI.begin(); // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card
  
  // Shows in serial that is ready to read - Affiche en série ce qui est prêt à être lu
  Serial.println(F("Read personal data on a MIFARE PICC:")); 

  Serial.println("Set Servo");

  // Attaches the servo on pin 9 to the servo object - Fixe le servo sur la broche 9 à l'objet servo
  doorservo.attach(DOORSERVO); 

  lastActionTime = millis();
}

bool checkCard() {
  if ( mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    Serial.println(F("**Card Detected:**"));
    return true;
  }

  return false;
}

void setDoor(bool openclose) {
  if (openclose) {
    // Open the door - Ouvre la porte
    Serial.println("Opening Door");
    doorservo.write(OPEN_ANGLE);
    status_info.dooropen = true;
  } else {
    // Close the door - Ferme la porte
    Serial.println("Closing Door");
    doorservo.write(CLOSED_ANGLE);
    status_info.dooropen = false;
  }
}

void loop() {
  // Check if card is true then we open or close the door
  // Vérifier si la carte est true, puis nous ouvrons ou fermons la porte
  if (checkCard()) {
      if (millis() > lastActionTime + 2000) {
        setDoor(!status_info.dooropen);
        lastActionTime = millis();
      }
  }
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
    
    if (command[0] == 'D') {
        // Set the Door - Règle la porte
        Serial.println(command[1]);
        
        if (command[1] == 'O') {
          setDoor(true);
        } else if (command[1] == 'C') {
          setDoor(false);
        } else {
          Serial.println(command[0]);
        }
     }
}

void sendData() {
  // Send humidity and temperature and leds data
  // Envoyer les données d'humidité et de température et les leds
  Wire.write((byte*)(&status_info),sizeof(status_info));  
}
