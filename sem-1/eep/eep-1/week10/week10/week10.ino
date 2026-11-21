/*
  Week 10 Capstone: Obstacle Avoiding Line Follower (AlphaBot2)

  What the robot does, in plain words:
  - Waits 4 seconds after you switch it on.
  - Drives along the white line on the black floor.
  - Where the road splits, it looks ahead:
      something in the way -> it turns onto the side road
      nothing in the way   -> it keeps going straight
  - Its 4 lights show what the floor sensors see: red = white, green = black.
  - When every floor sensor sees white, it has reached the END box:
    it stops and beeps 3 times.
*/

////////////////////////////////////////////////////////////////////////////////
//CODE STARTS


// ================= LIBRARIES =================
// Libraries are ready-made code written by someone else, so we don't have to.
#include <IRArray.h>            // lets us read the 5 floor sensors
#include <Wire.h>               // lets the Arduino talk to other chips using 2 wires
#include <Adafruit_PCF8574.h>   // lets us control the small chip the beeper is plugged into
#include <Adafruit_NeoPixel.h>  // lets us control the 4 coloured lights


// ================= PIN DEFINITIONS =================
// A "pin" is a metal leg on the Arduino that a wire connects to.
// Here we give each pin an easy name, so the code says what it means.
#define TRIG_PIN 3    // tells the distance sensor to make a sound
#define ECHO_PIN 2    // hears the sound come back
#define NUM_LEDS 4    // there are 4 coloured lights
#define LED_PIN 7     // the one wire that controls all 4 lights
#define AIN1 A0       // left wheel: which way to spin (part 1)
#define AIN2 A1       // left wheel: which way to spin (part 2)
#define PWMA 6        // left wheel: how fast
#define BIN1 A3       // right wheel: which way to spin (part 1)
#define BIN2 A2       // right wheel: which way to spin (part 2)
#define PWMB 5        // right wheel: how fast
#define BUZZER_PIN 5  // the beeper (on the helper chip, not on the Arduino itself)


// ================= SETTINGS =================
#define THRESHOLD 959         // floor sensor number above this = white, below = black
#define BASE_SPEED 65         // normal speed (0 = stopped, 255 = full speed)
#define MAX_SPEED 120         // top speed a wheel is allowed
#define OBSTACLE_DISTANCE 25  // something closer than 25 cm = road is blocked


// ================= STEERING SETTINGS =================
float Kp = 24.0;   // how hard to steer back when the robot is off the line
float Kd = 371.0;  // calms the steering down so the robot doesn't wobble


// ================= THINGS WE USE =================
IRArray ir;                                                                          // the floor sensors
unsigned int sensorValues[5];                                                        // 5 boxes holding what each floor sensor sees (bigger = brighter)
Adafruit_PCF8574 pcf;                                                                // the helper chip with the beeper
Adafruit_NeoPixel RGB = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);  // the 4 lights


// ================= THINGS THE ROBOT REMEMBERS =================
int weights[5] = { 2, 1, 0, -1, -2 };  // a score for where each sensor sits: middle = 0, edges = 2 or -2
float lastKnownError = 0;              // where the line was the last time we saw it
float previousError = 0;               // where the line was a moment ago


// ================= WHEELS =================
// Makes both wheels roll forward, each at its own speed.
// Same speed = straight. Different speeds = the robot turns toward the slower wheel.
void moveForward(int leftSpeed, int rightSpeed) {
  digitalWrite(AIN1, HIGH);      // these two lines make the left wheel
  digitalWrite(AIN2, LOW);       // spin forward
  analogWrite(PWMA, leftSpeed);  // set the left wheel's speed

  digitalWrite(BIN1, HIGH);       // these two lines make the right wheel
  digitalWrite(BIN2, LOW);        // spin forward
  analogWrite(PWMB, rightSpeed);  // set the right wheel's speed
}

// Stops both wheels.
void stopMotors() {
  digitalWrite(AIN1, LOW);  // left wheel: no direction
  digitalWrite(AIN2, LOW);
  analogWrite(PWMA, 0);  // left wheel: speed 0

  digitalWrite(BIN1, LOW);  // right wheel: no direction
  digitalWrite(BIN2, LOW);
  analogWrite(PWMB, 0);  // right wheel: speed 0
}


// ================= DISTANCE SENSOR, BEEPER, LIGHTS =================
// Finds out how far away the thing in front is, in cm.
// It works like a bat: make a sound, time how long the echo takes.
long readDistance() {
  digitalWrite(TRIG_PIN, LOW);   // be quiet first
  delayMicroseconds(2);          // wait a tiny moment
  digitalWrite(TRIG_PIN, HIGH);  // "shout"...
  delayMicroseconds(10);         // ...for a tiny moment
  digitalWrite(TRIG_PIN, LOW);   // stop shouting

  long duration = pulseIn(ECHO_PIN, HIGH, 25000);  // time how long the echo takes (give up if too long)
  if (duration == 0) return 100;                   // no echo = nothing in front, say 100 cm
  return duration / 58;                            // turn the echo time into cm
}

// Beeps the beeper a number of times.
// Note: on this robot, LOW turns the beeper ON and HIGH turns it OFF.
void beepBuzzer(int times) {
  for (int i = 0; i < times; i++) {      // repeat this as many times as asked
    pcf.digitalWrite(BUZZER_PIN, LOW);   // beeper ON
    delay(200);                          // wait 0.2 seconds
    pcf.digitalWrite(BUZZER_PIN, HIGH);  // beeper OFF
    delay(150);                          // wait 0.15 seconds
  }
}

// Makes the 4 lights show what 4 of the floor sensors see.
// (There are 5 sensors but only 4 lights, so the middle sensor gets no light.)
void updateSensorLEDs() {
  int displayIndices[4] = { 0, 1, 3, 4 };  // which sensor goes with which light (skip the middle one)
  for (int i = 0; i < 4; i++) {            // do this for each of the 4 lights
    int sensorIdx = displayIndices[i];     // find this light's sensor
    if (sensorValues[sensorIdx] > THRESHOLD) {
      RGB.setPixelColor(i, RGB.Color(255, 0, 0));  // sensor sees white -> light goes red
    } else {
      RGB.setPixelColor(i, RGB.Color(0, 255, 0));  // sensor sees black -> light goes green
    }
  }
  RGB.show();  // actually turn the lights on with the new colours
}


// ================= WHERE IS THE LINE? =================
// Gives back a number that says where the white line is under the robot:
//   0           = line is right in the middle (good, go straight)
//   bigger/smaller than 0 = line is off to one side (steer back)
// If no sensor can see the line, it uses the last place the line was seen.
float readError() {

  ir.read(sensorValues);  // look at the floor with all 5 sensors

  int whiteCount = 0;     // how many sensors see the white line
  float weightedSum = 0;  // add up the scores of those sensors

  for (int i = 0; i < 5; i++) {                // check each sensor, one by one
    if (sensorValues[i] > THRESHOLD) {         // this sensor sees white
      weightedSum = weightedSum + weights[i];  // add its score
      whiteCount = whiteCount + 1;             // count it
    }
  }

  if (whiteCount == 0) {    // no sensor sees the line (robot drifted off)
    return lastKnownError;  // use where the line was last time
  }

  lastKnownError = weightedSum / whiteCount;  // average score = where the line is; remember it
  return lastKnownError;                      // give the answer back
}


// ================= SETUP =================
// This part runs only once, right when you switch the robot on.
void setup() {

  pinMode(AIN1, OUTPUT);  // the wheel wires send orders out
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);

  pinMode(TRIG_PIN, OUTPUT);  // this wire sends the "shout"
  pinMode(ECHO_PIN, INPUT);   // this wire listens for the echo

  pcf.begin(0x20, &Wire);              // connect to the helper chip (0x20 is its address)
  pcf.pinMode(BUZZER_PIN, OUTPUT);     // the beeper wire sends orders out
  pcf.digitalWrite(BUZZER_PIN, HIGH);  // make sure the beeper is OFF

  RGB.begin();  // get the lights ready
  RGB.show();   // start with all lights off

  ir.begin();  // get the floor sensors ready

  stopMotors();  // make sure the wheels are not moving

  delay(4000);  // wait 4 seconds so you can put the robot down, walk away and start the camera
}


// ================= LOOP =================
// This part repeats again and again, very fast, until the robot is switched off.
// Each time: look at the floor -> decide what to do -> move the wheels.
void loop() {

  // 1. Find where the line is
  float error = readError();

  // 2. Update the lights
  updateSensorLEDs();

  // 3. Count how many sensors see white
  int whiteCount = 0;                   // start counting from 0
  for (int i = 0; i < 5; i++) {         // check all 5 sensors
    if (sensorValues[i] > THRESHOLD) {  // this one sees white
      whiteCount++;                     // add 1 to the count
    }
  }

  // 4. All 5 sensors see white = we are on the white END box. Finish!
  if (whiteCount == 5) {
    stopMotors();  // stop
    for (int i = 0; i < 4; i++) {
      RGB.setPixelColor(i, RGB.Color(255, 0, 0));  // make all lights red
    }
    RGB.show();      // turn the lights on
    beepBuzzer(3);   // beep 3 times
    while (1) {      // stay here forever...
      stopMotors();  // ...with the wheels stopped, so the robot never moves again
    }
  }

  // 5. 3 or more sensors see white = the road splits here (a junction)
  if (whiteCount >= 3) {
    long distance = readDistance();       // check: is something in front?
    if (distance <= OBSTACLE_DISTANCE) {  // yes, the road ahead is blocked -> take the side road
      // which side is the side road on? check the sensors on one side
      if (sensorValues[0] > THRESHOLD || sensorValues[1] > THRESHOLD) {
        moveForward(0, BASE_SPEED);  // stop one wheel, keep the other going = turn one way
      } else {
        moveForward(BASE_SPEED, 0);  // stop the other wheel = turn the other way
      }
      delay(550);  // keep turning for about half a second
      return;      // start the loop again from the top
    }
    // nothing in front -> do nothing special, just keep following the line straight
  }

  // 6. Steer to stay on the line
  float derivative = error - previousError;             // how quickly the robot is drifting off
  float correction = (Kp * error) + (Kd * derivative);  // how much to steer to get back

  int leftSpeed = BASE_SPEED - correction;   // slow one wheel down...
  int rightSpeed = BASE_SPEED + correction;  // ...and speed the other up, so the robot turns back onto the line

  leftSpeed = constrain(leftSpeed, 0, MAX_SPEED);  // don't let the speed go below 0 or above the top speed
  rightSpeed = constrain(rightSpeed, 0, MAX_SPEED);

  moveForward(leftSpeed, rightSpeed);  // move the wheels at these speeds

  previousError = error;  // remember where the line was, for next time
}
