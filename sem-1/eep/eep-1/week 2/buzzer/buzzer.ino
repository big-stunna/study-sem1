/*
  Week 2 — Activity: Buzzer Control

  Learning objectives:
  - Use the Adafruit PCF8574 library
  - Control the onboard buzzer via the I/O expander
  - Create beep patterns using delay()

  Instructions:
  - The buzzer is on PCF8574 pin 5
  - LOW = buzzer ON, HIGH = buzzer OFF (active LOW)
  - Uncomment and fill in the blanks marked with _______
  - Make the buzzer beep 3 times with 200ms ON and 200ms OFF
*/

////////////////////////////////////////////////////////////////////////////////
                              //CODE STARTS


// ================= LIBRARIES =================
#include <Wire.h>               // required for I²C communication
#include <Adafruit_PCF8574.h>   // Adafruit library for PCF8574 I/O expander

// ================= OBJECT =================
Adafruit_PCF8574 pcf;           // create a PCF8574 object named 'pcf'

// ================= CONSTANTS =================
#define BUZZER_PIN  5           // buzzer is on PCF8574 pin 5

// ================= SETUP =================
void setup() {
  // initialise the PCF8574 at I²C address 0x20 — fill in the address
  pcf.begin(0x20 , &Wire);

  // set the buzzer pin as an output on the PCF8574 — fill in pin and mode
  pcf.pinMode(5, OUTPUT);

  // make sure buzzer is off at startup — HIGH = OFF for active LOW buzzer
  pcf.digitalWrite(HIGH, LOW);
}


// ================= LOOP =================
void loop() {

  // beep the buzzer 3 times
  // 'i' starts at 0, runs while i < 3, increases by 1 each time

  for (int i = 0; i < 3; i++) {

    // turn buzzer ON — remember: LOW = ON for this buzzer
    pcf.digitalWrite(5, LOW);
    delay(1000);    // wait 200ms

    // turn buzzer OFF — HIGH = OFF
    pcf.digitalWrite(5, HIGH);
    delay(1000);    // wait 200ms between beeps

  }

  delay(2000);    // wait 2 seconds before repeating the beep sequence
}