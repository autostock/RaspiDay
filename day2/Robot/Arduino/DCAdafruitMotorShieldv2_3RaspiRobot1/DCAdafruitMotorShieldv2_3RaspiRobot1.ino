/* 
This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
It won't work with v1.x motor shields! Only for the v2's with built in PWM
control

For use with the Adafruit Motor Shield v2 
---->	http://www.adafruit.com/products/1438
*/

#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61); 

// Select which 'port' M1, M2, M3 or M4. In this case, M1
Adafruit_DCMotor *myMotor1 = AFMS.getMotor(1);
Adafruit_DCMotor *myMotor2 = AFMS.getMotor(2);
// You can also make another motor on port M2
//Adafruit_DCMotor *myOtherMotor = AFMS.getMotor(2);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  //Serial.println("Adafruit Motorshield v2 - robot!");

  AFMS.begin();  // create with the default frequency 1.6KHz
  
  myMotor1->run(RELEASE);
  myMotor2->run(RELEASE);
}

void loop() {
  static int debug;
  int speed;

  if (Serial.available()) {
    int c=Serial.read();
    switch(c) {
      case 'd':
      case 'D':
        debug ^=1;
        Serial.print("> debug "); Serial.println(debug);
        break;  
      case 'f':
        speed=Serial.parseInt();
        myMotor1->run(FORWARD);
        myMotor1->setSpeed(speed);
        if (debug) {
          Serial.print("> f "); Serial.println(speed);
        }
        break;  
      case 'b':
        speed=Serial.parseInt();
        myMotor1->run(BACKWARD);
        myMotor1->setSpeed(speed);
        if (debug) {
          Serial.print("> b "); Serial.println(speed);
        }
        break;  
      case 'r':
        myMotor1->run(RELEASE);
        if (debug) {
          Serial.println("> r");
        }
        break;  
      case 'F':
        speed=Serial.parseInt();
        myMotor2->run(FORWARD);
        myMotor2->setSpeed(speed);
        if (debug) {
          Serial.print("> F "); Serial.println(speed);
        }
        break;  
      case 'B':
        speed=Serial.parseInt();
        myMotor2->run(BACKWARD);
        myMotor2->setSpeed(speed);
        if (debug) {
          Serial.print("> B "); Serial.println(speed);
        }
        break;  
      case 'R':
        myMotor2->run(RELEASE);
        if (debug) {
          Serial.println("> R");
        }
        break;  
    }
  }
}
