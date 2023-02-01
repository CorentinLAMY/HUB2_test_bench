String command;

void setup() {

Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
pinMode(LED_BUILTIN, OUTPUT);
digitalWrite(LED_BUILTIN, HIGH);
delay(300);
digitalWrite(LED_BUILTIN, LOW);

}

void loop() {

  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    
    if (command.equals("H")){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
    }else if (command.equals("A")){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(300);
      digitalWrite(LED_BUILTIN, LOW);
      delay(300);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(300);
    }
    digitalWrite(LED_BUILTIN, LOW);
  }
}