/*
  Week 10 Capstone: Obstacle Avoiding Line Follower (AlphaBot2)
  - Start delay, then follow the white line with PD control
  - Junction (3+ sensors white): obstacle ahead -> take branch, clear -> go straight
  - LEDs show IR1, IR2, IR4, IR5: red = white, green = black
  - END (all 5 white): stop, beep 3 times
*/

////////////////////////////////////////////////////////////////////////////////
                              //CODE STARTS


// ================= LIBRARIES =================
#include <IRArray.h>            // 5 IR line sensors
#include <Wire.h>               // I2C bus (for PCF8574)
#include <Adafruit_PCF8574.h>   // I/O expander; buzzer is on it
#include <Adafruit_NeoPixel.h>  // 4 RGB LEDs


// ================= PIN DEFINITIONS =================
#define TRIG_PIN  3     // ultrasonic: sends pulse
#define ECHO_PIN  2     // ultrasonic: receives echo
#define NUM_LEDS 4      // LED count
#define LED_PIN 7       // one data pin drives all 4 LEDs
#define AIN1   A0       // left motor direction
#define AIN2   A1       // left motor direction
#define PWMA   6        // left motor speed (PWM)
#define BIN1   A3       // right motor direction
#define BIN2   A2       // right motor direction
#define PWMB   5        // right motor speed (PWM)
#define BUZZER_PIN  5   // pin P5 on the PCF8574, not Arduino pin 5


// ================= CONSTANTS =================
#define THRESHOLD    900        // reading > this = white
#define BASE_SPEED   50         // cruising speed (0-255)
#define MAX_SPEED    50         // speed limit per wheel
#define OBSTACLE_DISTANCE  25   // cm; closer = obstacle


// ================= TUNING =================
float Kp = 20.0;    // P gain: steer harder the further off the line
float Kd = 395.0;   // D gain: damps wobble


// ================= OBJECTS =================
IRArray ir;                       // line sensors
unsigned int sensorValues[5];     // readings 0-1023; [0] = IR1 ... [4] = IR5
Adafruit_PCF8574 pcf;             // buzzer chip
Adafruit_NeoPixel RGB = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);   // LED strip


// ================= VARIABLES =================
int   weights[5] = { 2, 1, 0, -1, -2 };   // sensor position scores; 0 = centre
float lastKnownError = 0;   // last error while line was visible
float previousError  = 0;   // last loop's error, for the D term


// ================= MOVEMENT FUNCTIONS =================
// Both wheels forward at their own speeds; robot turns toward the slower one.
void moveForward(int leftSpeed, int rightSpeed) {
  digitalWrite(AIN1, HIGH);        // left: HIGH + LOW = forward
  digitalWrite(AIN2, LOW);
  analogWrite(PWMA, leftSpeed);    // left speed

  digitalWrite(BIN1, HIGH);        // right: HIGH + LOW = forward
  digitalWrite(BIN2, LOW);
  analogWrite(PWMB, rightSpeed);   // right speed
}

// Both wheels off.
void stopMotors() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  analogWrite(PWMA, 0);

  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMB, 0);
}


// ================= SENSORS & BUZZER =================
// Distance ahead in cm.
long readDistance() {
  digitalWrite(TRIG_PIN, LOW);     // clean start
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);    // 10 us pulse = send sound
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH, 25000);   // echo time (us); give up after 25 ms
  if (duration == 0) return 100;                    // no echo = road clear
  return duration / 58;                             // us -> cm (there and back)
}

// Beep n times. Buzzer is active LOW.
void beepBuzzer(int times) {
  for (int i = 0; i < times; i++) {
    pcf.digitalWrite(BUZZER_PIN, LOW);    // ON
    delay(200);
    pcf.digitalWrite(BUZZER_PIN, HIGH);   // OFF
    delay(150);
  }
}

// LEDs 0-3 show IR1, IR2, IR4, IR5 (IR3 has no LED).
void updateSensorLEDs() {
  int displayIndices[4] = {0, 1, 3, 4};   // sensor shown on each LED
  for (int i = 0; i < 4; i++) {
    int sensorIdx = displayIndices[i];
    if (sensorValues[sensorIdx] > THRESHOLD) {
      RGB.setPixelColor(i, RGB.Color(255, 0, 0));   // white -> red
    } else {
      RGB.setPixelColor(i, RGB.Color(0, 255, 0));   // black -> green
    }
  }
  RGB.show();   // apply colours
}


// ================= ERROR FUNCTION =================
// Error = average weight of sensors seeing white (0 = centred, sign = side).
// Line lost -> return last error so the robot keeps turning the same way.
float readError() {

  ir.read(sensorValues);   // fresh readings

  int   whiteCount  = 0;   // sensors on the line
  float weightedSum = 0;   // sum of their weights

  for (int i = 0; i < 5; i++) {
    if (sensorValues[i] > THRESHOLD) {          // white line = high reading
      weightedSum = weightedSum + weights[i];
      whiteCount  = whiteCount + 1;
    }
  }

  if (whiteCount == 0) {   // line lost
    return lastKnownError;
  }

  lastKnownError = weightedSum / whiteCount;   // average = error; save it
  return lastKnownError;
}


// ================= SETUP =================
// Runs once at power-on.
void setup() {

  pinMode(AIN1, OUTPUT);   // motor pins
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);

  pinMode(TRIG_PIN, OUTPUT);   // ultrasonic: send
  pinMode(ECHO_PIN, INPUT);    // ultrasonic: listen

  pcf.begin(0x20, &Wire);               // PCF8574 at I2C address 0x20
  pcf.pinMode(BUZZER_PIN, OUTPUT);
  pcf.digitalWrite(BUZZER_PIN, HIGH);   // buzzer off

  RGB.begin();   // LEDs on, all dark
  RGB.show();

  ir.begin();    // line sensors on

  stopMotors();

  delay(4000);   // start delay: place robot, step away, start recording
}


// ================= LOOP =================
// Repeats forever: sense -> decide -> drive.
void loop() {

  // 1. Where is the line?
  float error = readError();

  // 2. Show sensors on LEDs
  updateSensorLEDs();

  // 3. Count sensors seeing white
  int whiteCount = 0;
  for (int i = 0; i < 5; i++) {
    if (sensorValues[i] > THRESHOLD) {
      whiteCount++;
    }
  }

  // 4. END: all 5 white -> stop, LEDs red, 3 beeps, halt forever
  if (whiteCount == 5) {
    stopMotors();
    for (int i = 0; i < 4; i++) {
      RGB.setPixelColor(i, RGB.Color(255, 0, 0));
    }
    RGB.show();
    beepBuzzer(3);
    while (1) {        // trap here; robot never moves again
      stopMotors();
    }
  }

  // 5. Junction: 3+ white (line widens at a branch)
  if (whiteCount >= 3) {
    long distance = readDistance();          // look ahead
    if (distance <= OBSTACLE_DISTANCE) {     // blocked -> take branch
      // pivot toward the side where IR1/IR2 see white, else the other way
      if (sensorValues[0] > THRESHOLD || sensorValues[1] > THRESHOLD) {
        moveForward(0, BASE_SPEED);          // left wheel stopped -> pivot
      }
      else {
        moveForward(BASE_SPEED, 0);          // right wheel stopped -> pivot
      }
      delay(550);                            // turn for 0.55 s (blind, timed)
      return;                                // restart loop()
    }
    // clear -> fall through; PD keeps going straight
  }

  // 6. PD steering
  float derivative = error - previousError;              // how fast error changes
  float correction = (Kp * error) + (Kd * derivative);   // amount to steer

  int leftSpeed  = BASE_SPEED - correction;   // opposite changes on each wheel
  int rightSpeed = BASE_SPEED + correction;   // -> robot turns toward the line

  leftSpeed  = constrain(leftSpeed,  0, MAX_SPEED);   // clamp to 0..MAX
  rightSpeed = constrain(rightSpeed, 0, MAX_SPEED);

  moveForward(leftSpeed, rightSpeed);

  previousError = error;   // save for next loop's D term
}
