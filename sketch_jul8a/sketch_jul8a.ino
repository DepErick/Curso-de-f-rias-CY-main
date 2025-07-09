void setup() {
  pinMode(2, OUTPUT);      // LED no pino 2
  Serial.begin(9600);      // Comunicação serial
}

void loop() {
  if (Serial.available()) {
    char comando = Serial.read();

    if (comando == '1') {
      digitalWrite(2, HIGH); // Liga o LED
    } else if (comando == '0') {
      digitalWrite(2, LOW);  // Desliga o LED
    }
  }
}
