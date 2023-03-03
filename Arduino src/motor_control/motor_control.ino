#include <Servo.h> //서보관련 라이브러리를 사용하기 위해

Servo servo1;  // 서보 변수 선언
Servo servo2;  // 서보 변수 선언
const int servo1Pin = 10; // 서보1 핀
const int servo2Pin = 9; // 서보2 핀

const int buttonPin2 = 2;
const int buttonPin3 = 3;
const int buttonPin4 = 4;
const int buttonPin5 = 5;

int servo1_degree = 90;
int servo2_degree = 90;

void setup() {
  servo1.attach(servo1Pin); 
  servo2.attach(servo2Pin);


  pinMode(buttonPin2, INPUT_PULLUP);
  pinMode(buttonPin3, INPUT_PULLUP);
  pinMode(buttonPin4, INPUT_PULLUP);
  pinMode(buttonPin5, INPUT_PULLUP);

}

void loop() {
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
  if (buttonValue3 == LOW) {
   
  }
  if (buttonValue4 == LOW) {

  }
  if (buttonValue5 == LOW) {

  }

  delay(10);

}
