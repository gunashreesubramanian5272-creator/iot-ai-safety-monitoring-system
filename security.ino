#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// LCD (try 0x27, if not working use 0x3F)
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Pins
int tempPin = A0;
int waterPin = A1;
int currentPin = A2;

int greenLED = 8;
int redLED = 7;
int buzzer = 9;
int relay = 6;

// Thresholds (adjust after testing)
int tempThreshold = 600;
int waterThreshold = 300;
int currentThreshold = 700;

void setup() {
  Serial.begin(9600);

  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(relay, OUTPUT);

  digitalWrite(relay, LOW); // Pump OFF initially

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0,0);
  lcd.print("System Starting");
  delay(2000);
  lcd.clear();
}

void loop() {

  // Read sensors
  int temp = analogRead(tempPin);
  int water = analogRead(waterPin);
  int current = analogRead(currentPin);

  // Serial Monitor Output
  Serial.print("Temp: "); Serial.print(temp);
  Serial.print(" | Water: "); Serial.print(water);
  Serial.print(" | Current: "); Serial.println(current);

  // LCD Display
  lcd.setCursor(0,0);
  lcd.print("T:");
  lcd.print(temp);
  lcd.print(" W:");
  lcd.print(water);
  lcd.print("   ");

  lcd.setCursor(0,1);
  lcd.print("C:");
  lcd.print(current);
  lcd.print("   ");

  // ALERT CONDITION
  if (temp > tempThreshold || water < waterThreshold || current > currentThreshold) {

    

    digitalWrite(greenLED, LOW);
    digitalWrite(redLED, HIGH);
    digitalWrite(buzzer, HIGH);
    digitalWrite(relay, LOW); // Pump OFF

    lcd.setCursor(10,1);
    lcd.print("SAFE ");
  }
else{
   digitalWrite(greenLED, HIGH);
    digitalWrite(redLED, LOW);
    digitalWrite(buzzer, LOW);
    digitalWrite(relay, HIGH); // Pump OFF

    lcd.setCursor(10,1);
    lcd.print("SAFE ");
  }

  delay(1000);
}