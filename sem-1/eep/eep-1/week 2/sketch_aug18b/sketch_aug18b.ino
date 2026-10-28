/*
  Week 2 — Activity: RGB LED Control

  Learning objectives:
  - Use the Adafruit NeoPixel library
  - Set individual LED colours using RGB.Color(r, g, b)
  - Use RGB.show() to push colour changes to the LEDs

  Instructions:
  - The AlphaBot2 has 4 NeoPixel LEDs on pin D7
  - Set each LED to a different colour in setup()
  - Call RGB.show() once after setting all four colours
  - Uncomment and fill in the blanks marked with _______
*/


////////////////////////////////////////////////////////////////////////////////
                              //CODE STARTS


// ================= LIBRARY =================
#include <Adafruit_NeoPixel.h>    // library for controlling WS2812B LEDs

// ================= CONSTANTS =================
#define NUM_LEDS 4                  // Number of LED's on AlphaBot2
#define LED_PIN 7                   // data pin for the LED chain on AlphaBot2

// ================= NEOPIXEL OBJECT =================
// creates a NeoPixel object named RGB
// arguments: (number of LEDs, data pin, LED type — do not change the last argument)
Adafruit_NeoPixel RGB = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);


// ================= SETUP =================
void setup() {
  // initialise the LED strip — always needed before using any LED functions
   RGB.begin();

  // set LED 0 (L1) to Red — fill in the correct R, G, B values
  RGB.setPixelColor(0, RGB.Color(255, 0, 0));

  // set LED 1 (L2) to Green
  RGB.setPixelColor(1, RGB.Color(0, 255, 0));

  // set LED 2 (L3) to Blue
  RGB.setPixelColor(2, RGB.Color(0, 0, 255));

  // set LED 3 (L4) to Yellow — hint: yellow is red + green mixed
  RGB.setPixelColor(3, RGB.Color(255, 255, 0));

  // send all colour data to the LEDs — nothing lights up without this line
  RGB.show();
}


// ================= LOOP =================
void loop() {
  // nothing here for now — colours are set once in setup()
  // you will add animations and patterns in the lab activity
}