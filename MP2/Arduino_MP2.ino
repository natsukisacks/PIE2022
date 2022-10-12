#include <Servo.h>

// Create servo objects
Servo base_servo;
Servo sensor_servo;

// Create variables to store information
int pos = 50;    // variable to store the base servo position
int angle = 0;   // variable to store tilt servo position
const int sensorPin = A0;
int sensorValue = 0;
int sum = 0;
int avgSensor = 0;
int i = 0;   // for loop incrementer

void setup() {
  base_servo.attach(9);
  sensor_servo.attach(10);
  Serial.begin(9600);
}

void loop() {
  sensor_servo.write(110);
  base_servo.write(70);

  // Move the servos!
  for (angle = 90; angle >= 30; angle -= 1) {
    for (pos = 50; pos <= 110; pos += 1) {
      sum = 0;   // Reset the sum variable after each new pan angle
      base_servo.write(pos);
      delay(30);
      sensor_servo.write(angle);

      // take the average of 30 points at each new angle
      for (i = 0; i <= 30; i += 1) {
        sensorValue = analogRead(sensorPin);
        sum += sensorValue;
      }
    avgSensor = sum / i;
     
    // Print information to serial monitor as "pan_angle tilt_angle avg_Sensor"
    Serial.print(pos); 
    Serial.print(" "); 
    Serial.print(angle);
    Serial.print(" ");
    Serial.print(avgSensor);
    delay(30);
    }
  }
}
