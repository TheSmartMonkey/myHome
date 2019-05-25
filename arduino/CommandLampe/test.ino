
const int LED_KITCHEN = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_KITCHEN,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    if (Serial.available()) {
      char cmd=char(Serial.read());
      if (cmd=='O'){
        digitalWrite(LED_KITCHEN,HIGH);
      }
      else if (cmd=='F'){
        digitalWrite(LED_KITCHEN,LOW);
      }
    }
  delay(10);
}
