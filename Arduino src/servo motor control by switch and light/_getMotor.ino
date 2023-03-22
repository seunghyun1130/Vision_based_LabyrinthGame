
#include "crc.h"
#include <Wire.h>

u16 crc16_ccitt(const void *buf, int len);
u16 CRC;
u8 CRC_H, CRC_L;


char* receiveEvent() {
  char inputData;
  char* outData[2];
  inputData = Wire.read(); 
  Serial.print("Receive Data : "); Serial.println(inputData); // decode 해야할 것 
  outData[0] = inputData[2]; outData[1] = inputData[3];

  char INITCRC[sizeof(inputData)-4];
  int len = sizeof(inputData);


  for(int i = 0; i < len-4; i++){
    INITCRC[i] = inputData[i+1];
  }


  CRC = crc16_ccitt(INITCRC, len-4);
  CRC_H = (CRC>>8);CRC_L = (CRC & 0xFF);

  if((CRC_H == inputData[-3])&&(CRC_L == inputData[-2])){
    return outData;
  }
  else{
    return false;
  }
}

void sendData(char ACK){
    Wire.write(ACK);
}

int getMotor1proto() {
    int myList[] = {1, 2, 3, 4, 5};
    int listSize = sizeof(myList) / sizeof(int);
    int *ptr1 = myList + 1;
   
    //Serial.print(*ptr);
    
    return myList[1];
  }


int getMotor2proto() {
    int myList[] = {1, 2, 3, 4, 5};
    int listSize = sizeof(myList) / sizeof(int);
    int *ptr2 = myList + 2;

    return myList[2];
  }

int getMotor1(char input) {
    int angle = input[0];
    return angle;
  }


int getMotor2(char input) {
    int angle = input[1];

    return angle;
  }

void logic(){
  char angles;
  angles = receiveEvent();
  getMotor1(angles);
  getMotor2(angles);
}