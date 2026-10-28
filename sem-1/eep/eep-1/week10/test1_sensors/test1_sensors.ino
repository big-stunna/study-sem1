// Test 1: print the 5 IR sensor readings and the ultrasonic distance
#include <IRArray.h>

#define TRIG_PIN 3
#define ECHO_PIN 2

IRArray ir;
unsigned int sensorValues[5];

void setup() {
  Serial.begin(115200);
  ir.begin();
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  ir.read(sensorValues);
  for (int i = 0; i < 5; i++) {
    Serial.print(sensorValues[i]);
    Serial.print('\t');
  }

  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  unsigned long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  Serial.print("dist: ");
  Serial.println(duration * 0.0343 / 2);

  delay(200);   // fine here: this test does not drive
}
