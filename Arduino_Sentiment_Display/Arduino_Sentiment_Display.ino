#include <LiquidCrystal.h>

const int green_led = 9;
const int yellow_led = 8;
const int red_led = 7;

// Initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  pinMode(green_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(red_led, OUTPUT);
  // Set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  // Check if data is available to read from the serial port
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n'); // Read the data until newline
    lcd.clear();  // Clear the display
    lcd.setCursor(0, 0); // Set the cursor to top-left position
    lcd.print(data); // Print new data on the LCD

    if (data == "Neutral"){
      digitalWrite(yellow_led, HIGH);
      delay(3000);
      digitalWrite(yellow_led, LOW);
    }
    else if (data == "Negative"){
      digitalWrite(red_led, HIGH);
      delay(3000);
      digitalWrite(red_led, LOW);
    }
    else if (data == "Positive"){
      digitalWrite(green_led, HIGH);
      delay(3000);
      digitalWrite(green_led, LOW);
    }
    delay(2000);
  }
}
