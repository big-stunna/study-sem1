
/*
  Week 2 - Activity: Serial Controlled Blinking LEDs

  Learning objectives:
  - Read a single serial command using Serial.available() and Serial.read()
  - Write separate functions for different actions and call them by name
  - Control 2 external LEDs based on serial commands

  Commands to implement:
  - '1' = LED 1 blinks 3 times
  - '2' = LED 2 blinks 3 times
  - '3' = Both LEDs blink together, 3 times

  Instructions:
  - 2 external LEDs are connected to pins 2 and 3
  - Uncomment lines in setup() and fill in the blanks marked with _______
*/

////////////////////////////////////////////////////////////////////////////////
                              //CODE STARTS


// ================= PIN DEFINITIONS =================
#define LED1_PIN  2
#define LED2_PIN  3

// ================= FUNCTION: blinkLed1 =================
// blinks LED 1 three times
void blinkLed1() {
  for (int i = 0; i < 3; i++) {
    digitalWrite(LED1_PIN, HIGH);
    delay(200);
    digitalWrite(LED1_PIN, LOW);
    delay(200);
  }
}

// ================= FUNCTION: blinkLed2 =================
// blinks LED 2 three times
void blinkLed2() {
  for (int i = 0; i < 3; i++) {
    digitalWrite(LED2_PIN, HIGH);
    delay(200);
    digitalWrite(LED2_PIN, LOW);
    delay(200);
  }
}

// ================= FUNCTION: blinkBoth =================
// TODO: Write this function yourself from scratch.
// It should blink both LEDs together, three times.
// Use blinkLed1() and blinkLed2() above as your reference for the pattern.
void blinkBoth(){
  for (int i = 0; i < 3; i++) {
    digitalWrite(LED2_PIN, HIGH);
    delay(200);
    digitalWrite(LED2_PIN, LOW);
    delay(200);
  }
   for (int i = 0; i < 3; i++) {
    digitalWrite(LED1_PIN, HIGH);
    delay(200);
    digitalWrite(LED1_PIN, LOW);
    delay(200);
  }

  

}

// ================= SETUP =================
void setup() {
  Serial.begin(9600);

  // set both LED pins as digital outputs - uncomment and fill in the pin names
  pinMode(2, OUTPUT);    // LED1
  pinMode(3, OUTPUT);    // LED2

  Serial.println("LED Console Ready. Commands: 1 | 2 | 3 ");
}

// ================= LOOP =================
void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    // '1' - blink LED1 three times
    if (command == '1') {
      blinkLed1();    // call blinkLed1
      Serial.println("LED 1 blinking");
    }

    // '2' - blink LED2 three times
    else if (command == '2') {
      blinkLed2();    // call blinkLed2
      Serial.println("LED 2 blinking");
    }

    // '3' - blink both LEDs together
    else if (command == '3') {
      blinkBoth();    // call blinkBoth
      Serial.println("Both LEDs blinking");
    }
  }
}