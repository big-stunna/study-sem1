/*
 * Week 10 Project: Obstacle Avoiding Line Follower
 * Hardware setup expected:
 *  - 4 Line / IR Sensors (S1, S2, S3, S4) mapped to 4 RGB LEDs (Green = White Line, Red = Ground/Black)
 *  - 1 Ultrasonic Sensor (Trig/Echo) or Distance Sensor for Obstacle Detection
 *  - 2 DC Motors (Left, Right) driven via PWM (e.g., L298N/L293D)
 *  - 1 Buzzer for End-of-Run indication
 */

// ==========================================
// 1. PIN CONFIGURATIONS (ADJUST TO YOUR BOARD)
// ==========================================
const int PIN_IR_S1 = A0; // Left Outer Sensor
const int PIN_IR_S2 = A1; // Left Inner Sensor
const int PIN_IR_S3 = A2; // Right Inner Sensor
const int PIN_IR_S4 = A3; // Right Outer Sensor

// Ultrasonic Distance Sensor Pins
const int PIN_TRIG  = 12; // Ultrasonic Trig pin
const int PIN_ECHO  = 13; // Ultrasonic Echo pin

// Motor Driver Pins (PWM capable pins for speed control)
const int PIN_ENA   = 5;  // PWM Left Motor
const int PIN_IN1   = 2;
const int PIN_IN2   = 3;
const int PIN_IN3   = 4;
const int PIN_IN4   = 7;
const int PIN_ENB   = 6;  // PWM Right Motor

// RGB LED Pins (paired with 4 IR sensors)
const int PIN_LED1_RED = 22, PIN_LED1_GREEN = 23;
const int PIN_LED2_RED = 24, PIN_LED2_GREEN = 25;
const int PIN_LED3_RED = 26, PIN_LED3_GREEN = 27;
const int PIN_LED4_RED = 28, PIN_LED4_GREEN = 29;

// Buzzer Pin
const int PIN_BUZZER = 8;


// ==========================================
// 2. TUNING PARAMETERS (TUNE THESE VALUES)
// ==========================================

// START DELAY
// TUNING PARAMETER: Delay in ms before robot starts moving after power-on/reset
const unsigned long START_DELAY_MS = 2000; 

// IR SENSOR THRESHOLDS
// TUNING PARAMETER: Adjust value based on Serial monitor reading for White line vs Dark background.
// Set high if reading digital HIGH on white, low if analog thresholding.
const int IR_THRESHOLD = 500; 

// OBSTACLE DETECTION THRESHOLD
// TUNING PARAMETER: Distance in cm to detect an obstacle at junctions/ahead.
const float OBSTACLE_DIST_CM = 15.0; 

// BASE MOTOR SPEEDS (0 - 255)
// TUNING PARAMETER: Base speed for straight line following. Higher = faster run time (T), lower = better stability.
const int BASE_SPEED = 140; 
const int MAX_SPEED  = 220; 
const int MIN_SPEED  = 0;

// PD CONTROLLER GAINS
// TUNING PARAMETER: Proportional gain (Kp) - Increase if response to turn is sluggish; decrease if it oscillates violently.
float Kp = 25.0; 

// TUNING PARAMETER: Derivative gain (Kd) - Increase to damp overshooting/wobble; decrease if robot jitters.
float Kd = 15.0; 

// JUNCTION & TURN TIMINGS
// TUNING PARAMETER: Duration (ms) needed to take a branch turn when an obstacle is detected.
const int BRANCH_TURN_TIME_MS = 450; 


// ==========================================
// 3. GLOBAL VARIABLES
// ==========================================
int lastError = 0;
bool runCompleted = false;

// ==========================================
// 4. HELPER FUNCTIONS
// ==========================================

// Read ultrasonic distance in centimeters
float readDistanceCM() {
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);
  
  long duration = pulseIn(PIN_ECHO, HIGH, 25000); // 25ms timeout
  if (duration == 0) return 999.0; // Return clear path if timeout
  return (duration * 0.0343) / 2.0;
}

// Drive motors with PWM speeds (-255 to 255)
void setMotors(int leftSpeed, int rightSpeed) {
  // Left motor direction
  if (leftSpeed >= 0) {
    digitalWrite(PIN_IN1, HIGH);
    digitalWrite(PIN_IN2, LOW);
  } else {
    digitalWrite(PIN_IN1, LOW);
    digitalWrite(PIN_IN2, HIGH);
    leftSpeed = -leftSpeed;
  }
  
  // Right motor direction
  if (rightSpeed >= 0) {
    digitalWrite(PIN_IN3, HIGH);
    digitalWrite(PIN_IN4, LOW);
  } else {
    digitalWrite(PIN_IN3, LOW);
    digitalWrite(PIN_IN4, HIGH);
    rightSpeed = -rightSpeed;
  }

  // Constrain speed values
  leftSpeed  = constrain(leftSpeed,  MIN_SPEED, MAX_SPEED);
  rightSpeed = constrain(rightSpeed, MIN_SPEED, MAX_SPEED);

  analogWrite(PIN_ENA, leftSpeed);
  analogWrite(PIN_ENB, rightSpeed);
}

// Stop both motors
void stopMotors() {
  analogWrite(PIN_ENA, 0);
  analogWrite(PIN_ENB, 0);
  digitalWrite(PIN_IN1, LOW);
  digitalWrite(PIN_IN2, LOW);
  digitalWrite(PIN_IN3, LOW);
  digitalWrite(PIN_IN4, LOW);
}

// Update paired RGB LEDs (Requirement 5)
void updateLEDs(bool s1, bool s2, bool s3, bool s4) {
  // S1 LED
  digitalWrite(PIN_LED1_GREEN, s1 ? HIGH : LOW);
  digitalWrite(PIN_LED1_RED,   s1 ? LOW  : HIGH);
  // S2 LED
  digitalWrite(PIN_LED2_GREEN, s2 ? HIGH : LOW);
  digitalWrite(PIN_LED2_RED,   s2 ? LOW  : HIGH);
  // S3 LED
  digitalWrite(PIN_LED3_GREEN, s3 ? HIGH : LOW);
  digitalWrite(PIN_LED3_RED,   s3 ? LOW  : HIGH);
  // S4 LED
  digitalWrite(PIN_LED4_GREEN, s4 ? HIGH : LOW);
  digitalWrite(PIN_LED4_RED,   s4 ? LOW  : HIGH);
}

// Sound buzzer 3 times upon reaching END box (Requirement 6)
void triggerEndSequence() {
  stopMotors();
  runCompleted = true;
  for (int i = 0; i < 3; i++) {
    digitalWrite(PIN_BUZZER, HIGH);
    delay(200);
    digitalWrite(PIN_BUZZER, LOW);
    delay(200);
  }
}

// ==========================================
// 5. SETUP & MAIN LOOP
// ==========================================

void setup() {
  // Pin modes setup
  pinMode(PIN_IR_S1, INPUT);
  pinMode(PIN_IR_S2, INPUT);
  pinMode(PIN_IR_S3, INPUT);
  pinMode(PIN_IR_S4, INPUT);

  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);

  pinMode(PIN_ENA, OUTPUT);
  pinMode(PIN_IN1, OUTPUT);
  pinMode(PIN_IN2, OUTPUT);
  pinMode(PIN_IN3, OUTPUT);
  pinMode(PIN_IN4, OUTPUT);
  pinMode(PIN_ENB, OUTPUT);

  pinMode(PIN_LED1_RED, OUTPUT); pinMode(PIN_LED1_GREEN, OUTPUT);
  pinMode(PIN_LED2_RED, OUTPUT); pinMode(PIN_LED2_GREEN, OUTPUT);
  pinMode(PIN_LED3_RED, OUTPUT); pinMode(PIN_LED3_GREEN, OUTPUT);
  pinMode(PIN_LED4_RED, OUTPUT); pinMode(PIN_LED4_GREEN, OUTPUT);

  pinMode(PIN_BUZZER, OUTPUT);

  stopMotors();

  // Requirement 1: Start delay
  delay(START_DELAY_MS);
}

void loop() {
  if (runCompleted) return;

  // Read sensors (True = detect white line)
  bool s1 = (analogRead(PIN_IR_S1) > IR_THRESHOLD);
  bool s2 = (analogRead(PIN_IR_S2) > IR_THRESHOLD);
  bool s3 = (analogRead(PIN_IR_S3) > IR_THRESHOLD);
  bool s4 = (analogRead(PIN_IR_S4) > IR_THRESHOLD);

  // Update RGB indicators (Requirement 5)
  updateLEDs(s1, s2, s3, s4);

  // Requirement 6: Check for END Box (All sensors on white line stop block)
  if (s1 && s2 && s3 && s4) {
    triggerEndSequence();
    return;
  }

  // Check for Junction (Inner or outer broad line trigger)
  bool isJunction = (s1 && s2) || (s3 && s4) || (s1 && s4);

  if (isJunction) {
    float distance = readDistanceCM();

    // Requirement 3: Obstacle ahead at junction -> Take branch
    if (distance < OBSTACLE_DIST_CM) {
      // TUNING PARAMETER: Branch turn direction/speed
      setMotors(-BASE_SPEED, BASE_SPEED); // Sharp Left Branch Turn
      delay(BRANCH_TURN_TIME_MS);
      return;
    } 
    // Requirement 4: Clear way ahead -> Carry on straight
    else {
      setMotors(BASE_SPEED, BASE_SPEED);
      delay(150); // TUNING PARAMETER: Forward pulse to clear junction mark
      return;
    }
  }

  // Requirement 2: Line Following using PD Controller
  // Calculate weighted error based on sensor positions
  // Left side negative, Right side positive
  int error = 0;
  if (s1 && !s2 && !s3 && !s4)      error = -3;
  else if (s1 && s2 && !s3 && !s4) error = -2;
  else if (!s1 && s2 && !s3 && !s4) error = -1;
  else if (!s1 && s2 && s3 && !s4)  error = 0;  // Centered
  else if (!s1 && !s2 && s3 && !s4) error = 1;
  else if (!s1 && !s2 && s3 && s4)  error = 2;
  else if (!s1 && !s2 && !s3 && s4)  error = 3;

  // PD Calculation
  int derivative = error - lastError;
  int correction = (Kp * error) + (Kd * derivative);
  lastError = error;

  // Calculate wheel speeds
  int leftMotorSpeed  = BASE_SPEED + correction;
  int rightMotorSpeed = BASE_SPEED - correction;

  setMotors(leftMotorSpeed, rightMotorSpeed);
}