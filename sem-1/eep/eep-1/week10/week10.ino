/*
  Week 10 Capstone — Obstacle Avoiding Line Follower
  White line on black track. PD control (from Week 9), ultrasonic junction
  decisions, RGB LED sensor dashboard, 3 beeps at END.
*/

#include <Wire.h>
#include <IRArray.h>
#include <Adafruit_PCF8574.h>
#include <Adafruit_NeoPixel.h>

// ================= PIN DEFINITIONS =================
#define AIN1 A0
#define AIN2 A1
#define PWMA 6
#define BIN1 A3
#define BIN2 A2
#define PWMB 5

#define TRIG_PIN 3
#define ECHO_PIN 2

#define BUZZER_PIN 5      // on PCF8574
#define LED_PIN 7
#define NUM_LEDS 4

// ================= TUNING =================
#define DEBUG 0               // 1 = print to Serial (set 0 for the final run)

#define START_DELAY_MS 8000   // time to place robot, walk out, start recording
#define THRESHOLD 500         // ABOVE this = WHITE (recalibrate on the arena!)
#define BASE_SPEED 70
#define MAX_SPEED 120
float Kp = 35;
float Kd = 400.0;

#define OBSTACLE_CM 25        // closer than this at a junction = blocked
#define US_INTERVAL_MS 15     // ultrasonic read period
#define JUNCTION_CONFIRM 2    // consecutive frames needed to accept a junction
#define BRANCH_MS 700         // how long to hug the branch side
#define STRAIGHT_MS 400       // how long to ignore outer sensors when going straight
#define JUNCTION_COOLDOWN_MS 800
#define END_CONFIRM 4         // consecutive all-white frames to accept END

// ================= OBJECTS =================
IRArray ir;
Adafruit_PCF8574 pcf;
Adafruit_NeoPixel RGB(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

unsigned int sensorValues[5];
bool white[5];
int weights[5] = {2, 1, 0, -1, -2};   // index 0 = left side

// ================= STATE =================
enum Mode { FOLLOW, BRANCH, STRAIGHT };
Mode mode = FOLLOW;
int branchSide = 0;                    // +1 = left, -1 = right
unsigned long modeStart = 0;
unsigned long lastJunctionEnd = 0;
unsigned long lastUsRead = 0;

float distanceCm = 999;
float lastKnownError = 0;
float previousError = 0;
int junctionCount = 0;
int endCount = 0;

// ================= MOVEMENT =================
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

// ================= SENSORS =================
void readSensors() {
  ir.read(sensorValues);
  for (int i = 0; i < 5; i++) {
    white[i] = sensorValues[i] > THRESHOLD;
  }
}

// average weight of white sensors in [from, to]; falls back to last error
float errorFrom(int from, int to) {
  int count = 0;
  float sum = 0;
  for (int i = from; i <= to; i++) {
    if (white[i]) {
      sum += weights[i];
      count++;
    }
  }
  if (count == 0) return lastKnownError;
  lastKnownError = sum / count;
  return lastKnownError;
}

void readUltrasonic() {
  if (millis() - lastUsRead < US_INTERVAL_MS) return;
  lastUsRead = millis();

  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // 6000 us timeout ~ 1 m, keeps the loop from blocking
  unsigned long duration = pulseIn(ECHO_PIN, HIGH, 6000);
  distanceCm = (duration == 0) ? 999 : duration * 0.0343 / 2;
}

// ================= LEDS / BUZZER =================
void updateLeds() {
  const int paired[4] = {0, 1, 3, 4};    // IR1, IR2, IR4, IR5 (IR3 has no LED)
  for (int i = 0; i < 4; i++) {
    uint32_t c = white[paired[i]] ? RGB.Color(255, 0, 0)   // white -> red
                                  : RGB.Color(0, 255, 0);  // black -> green
    RGB.setPixelColor(i, c);
  }
  RGB.show();
}

void beep(int times) {
  for (int i = 0; i < times; i++) {
    pcf.digitalWrite(BUZZER_PIN, LOW);   // ON
    delay(200);
    pcf.digitalWrite(BUZZER_PIN, HIGH);  // OFF
    delay(200);
  }
}

// ================= JUNCTION DETECTION =================
// returns +1 (branch on left), -1 (branch on right), 0 (none)
int detectJunction() {
  bool centre = white[1] || white[2] || white[3];
  if (centre && white[0] && !white[4]) return +1;
  if (centre && white[4] && !white[0]) return -1;
  return 0;
}

// ================= SETUP =================
void setup() {
  Serial.begin(115200);

  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  ir.begin();

  pcf.begin(0x20, &Wire);
  pcf.pinMode(BUZZER_PIN, OUTPUT);
  pcf.digitalWrite(BUZZER_PIN, HIGH);    // buzzer off

  RGB.begin();
  RGB.clear();
  RGB.show();

  stopMotors();
  delay(START_DELAY_MS);
}

// ================= LOOP =================
void loop() {
  readSensors();
  readUltrasonic();
  updateLeds();

  // ---- END: all five sensors white ----
  if (white[0] && white[1] && white[2] && white[3] && white[4]) {
    if (++endCount >= END_CONFIRM) {
      stopMotors();
      for (int i = 0; i < NUM_LEDS; i++) RGB.setPixelColor(i, RGB.Color(255, 0, 0));
      RGB.show();
      beep(3);
      while (true) {}
    }
  } else {
    endCount = 0;
  }

  unsigned long now = millis();

  // ---- junction decision ----
  if (mode == FOLLOW && now - lastJunctionEnd > JUNCTION_COOLDOWN_MS) {
    int side = detectJunction();
    junctionCount = side ? junctionCount + 1 : 0;
    if (junctionCount >= JUNCTION_CONFIRM) {
      junctionCount = 0;
      branchSide = side;
      modeStart = now;
      mode = (distanceCm < OBSTACLE_CM) ? BRANCH : STRAIGHT;
#if DEBUG
      Serial.print(mode == BRANCH ? "BRANCH " : "STRAIGHT ");
      Serial.print(side > 0 ? "L " : "R ");
      Serial.println(distanceCm);
#endif
    }
  }

  // ---- error by mode ----
  float error;
  if (mode == BRANCH) {
    // follow only the branch half so the robot locks onto the side road
    error = (branchSide > 0) ? errorFrom(0, 2) : errorFrom(2, 4);
    if (now - modeStart > BRANCH_MS) { mode = FOLLOW; lastJunctionEnd = now; }
  } else if (mode == STRAIGHT) {
    // ignore outer sensors so the branch does not pull the robot off
    error = errorFrom(1, 3);
    if (now - modeStart > STRAIGHT_MS) { mode = FOLLOW; lastJunctionEnd = now; }
  } else {
    error = errorFrom(0, 4);
  }

  // ---- PD (Week 9) ----
  float derivative = error - previousError;
  float correction = (Kp * error) + (Kd * derivative);
  previousError = error;

  int leftSpeed = constrain(BASE_SPEED - correction, 0, MAX_SPEED);
  int rightSpeed = constrain(BASE_SPEED + correction, 0, MAX_SPEED);
  moveForward(leftSpeed, rightSpeed);
}
