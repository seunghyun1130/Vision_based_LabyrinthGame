#include <Servo.h> //서보관련 라이브러리를 사용하기 위해
#include <Wire.h>
#include "config.h"
#include "crc.h"

Servo servo1;  // 서보 변수 선언
Servo servo2;  // 서보 변수 선언


int state = 1;
int a;
int b;
int getMotor1();
int getMotor2();


void setup() {

  servo1.attach(servo1Pin); 
  servo2.attach(servo2Pin);

  Serial.begin(9600);
  getMotor1();
  getMotor2();
  pinMode(buttonPin2, INPUT_PULLUP);
  pinMode(buttonPin3, INPUT_PULLUP);
  pinMode(buttonPin4, INPUT_PULLUP);
  pinMode(buttonPin5, INPUT_PULLUP);
  pinMode(ledR,OUTPUT);
  pinMode(ledB,OUTPUT);

  Wire.onReceive(receiveEvent);
  Wire.onRequest(sendData);

}

void loop() {


  a = getMotor1();
  b = getMotor2();
  Serial.print(a);
  Serial.println(b);

  while(state==1)
  {
    servo1.write(servo1_degree);
    servo2.write(servo2_degree);

    if(digitalRead(buttonPin3)==LOW)
    {
      state=0;
      Serial.println("ON");
      digitalWrite(ledR,LOW);
      digitalWrite(ledB,HIGH);
      break;
    }
  }

  while(state==0)
  {
    int X = analogRead(0);
    int Y = analogRead(1);

    int buttonValue2 = digitalRead(2);
    int buttonValue3 = digitalRead(3);
    int buttonValue4 = digitalRead(4);
    int buttonValue5 = digitalRead(5);

    if (X > 500) {
      servo1_degree = servo1_degree + 2;
      if (servo1_degree > 180) servo1_degree=180;
      servo1.write(servo1_degree);
    }


    if (X < 200) {
      servo1_degree = servo1_degree - 2;
      if (servo1_degree < 0) servo1_degree=0;
      servo1.write(servo1_degree);
    }
  

    if (Y > 500) {
      servo2_degree = servo2_degree + 2;
      if (servo2_degree > 180) servo2_degree=180;
      servo2.write(servo2_degree);
    }
  

    if (Y < 200) {
      servo2_degree = servo2_degree - 2;
      if (servo2_degree < 0) servo2_degree=0;
      servo2.write(servo2_degree);
    }
  

    if (buttonValue2 == LOW) {
      servo1.write(90);
      servo2.write(90);
      servo1_degree = 90;
      servo2_degree = 90;

    }

    if (buttonValue4 == LOW) {
      state=1;
      Serial.println("OFF");
      digitalWrite(ledR,HIGH);
      digitalWrite(ledB,LOW);
      delay(100);
      break;
    }
    if (buttonValue5 == LOW) {

    }

    delay(10);




  }








  }
