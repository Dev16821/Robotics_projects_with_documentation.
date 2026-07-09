void setup() {
    Serial.begin(38400);
}

void loop() {
    int value = analogRead(A0);
    Serial.println(value);
    delay(100);
}
