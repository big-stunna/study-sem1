#include <IRArray.h>

// ================= PIN DEFINITIONS =================
#define AIN1 A0
#define AIN2 A1
#define PWMA 6
#define BIN1 A3
#define BIN2 A2
#define PWMB 5

// ================= CONSTANTS =================
#define THRESHOLD 500
#define BASE_SPEED 70
#define MAX_SPEED 120

// ================= TUNING =================
float Kp = 35;
float Kd = 400.0;

// ================= OBJECTS =================
IRArray ir;
unsigned int sensorValues[5];

// ================= VARIABLES =================
int weights[5] = {2, 1, 0, -1, -2};

float lastKnownError = 0;
float previousError = 0;

// ================= MOVEMENT FUNCTIONS =================
void moveForward(int leftSpeed, int rightSpeed) {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);

  analogWrite(PWMA, leftSpeed);
  analogWrite(PWMB, rightSpeed);
}

void stopMotors() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);

  analogWrite(PWMA, 0);
  analogWrite(PWMB, 0);
}

// ================= ERROR FUNCTION =================
float readError() {

  ir.read(sensorValues);

  int blackCount = 0;
  float weightedSum = 0;

  for (int i = 0; i < 5; i++) {

    if (sensorValues[i] < THRESHOLD) {
      weightedSum += weights[i];
      blackCount++;
    }
  }

  if (blackCount == 0) {
    return lastKnownError;
  }

  lastKnownError = weightedSum / blackCount;

  return lastKnownError;
}

// ================= SETUP =================
void setup() {

  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);

  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);

  ir.begin();

  stopMotors();
  delay(1000);
}

// ================= LOOP =================
void loop() {

  float error = readError();

  // Calculate derivative
  float derivative = error - previousError;

  // PD correction
  float correction = (Kp * error) + (Kd * derivative);

  // Calculate motor speeds
  int leftSpeed = BASE_SPEED - correction;
  int rightSpeed = BASE_SPEED + correction;

  // Limit motor speeds
  leftSpeed = constrain(leftSpeed, 0, MAX_SPEED);
  rightSpeed = constrain(rightSpeed, 0, MAX_SPEED);

  // Apply corrected speeds
  moveForward(leftSpeed, rightSpeed);

  // Store error for next iteration
  previousError = error;
}