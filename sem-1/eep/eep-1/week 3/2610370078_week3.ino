/*
  Week 3 — Graded Activity: Circular Motion Challenge

  Learning objectives:
  - Use differential wheel speed to trace circular arcs
  - Understand the relationship between speed ratio and arc radius
  - Combine direction and speed control in a single sketch

  Instructions:
  - Complete the circleArc() function
  - Demonstrate three clearly different arc radii from setup()
  - Make sure neither speed value is below your dead-band threshold
  - Print the speed values before each arc
*/

////////////////////////////////////////////////////////////////////////////////
                              //CODE STARTS


// ================= PIN DEFINITIONS =================
#define AIN1   A1
#define AIN2   A0
#define PWMA   6
#define BIN1   A2
#define BIN2   A3
#define PWMB   5


// ================= MOVEMENT FUNCTIONS =================
// copy your completed stopMotors() function here
void stopMotors() {
  // both motors coast: all direction pins LOW, speed 0
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMA, 0);
  analogWrite(PWMB, 0);
}

// ================= CIRCLE ARC FUNCTION =================

void circleArc(int leftSpeed, int rightSpeed) {
  // both motors run forward but at different speeds
  // the faster wheel is on the outside of the arc

  // set both motors to forward direction
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);

  // apply the two different speed values
  analogWrite(PWMA, leftSpeed);    // left motor speed
  analogWrite(PWMB, rightSpeed);    // right motor speed
}


// ================= SETUP =================
void setup() {
  Serial.begin(9600);

  // set all six pins as OUTPUT
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);
}


// ================= LOOP =================
void loop() {

  // Arc 1: Wide arc — small speed difference
  Serial.println("Wide arc...");
  circleArc(180, 140);    // e.g. 180 and 140
  delay(3000);
  stopMotors();
  delay(1000);

  // Arc 2: Medium circle — medium speed difference
  Serial.println("Medium circle...");
  circleArc(180, 100);    // e.g. 180 and 100
  delay(3000);
  stopMotors();
  delay(1000);

  // Arc 3: Tight circle — large speed difference
  Serial.println("Tight circle...");
  circleArc(200, 70);    // e.g. 180 and 50
  delay(3000);
  stopMotors();
  delay(1000);
  
  Serial.println("Circular motion challenge complete.");
}