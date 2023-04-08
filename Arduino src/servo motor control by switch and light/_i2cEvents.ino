#include "crc.h"
#include <Wire.h>

u16 crc16_ccitt(const void *buf, int len);
u16 CRC;
u8 CRC_H, CRC_L;


char* receiveEvent(int bytes) {
  char inputData;
  char* outData[2];
  inputData = Wire.read();
  Serial.print("Receive Data : "); Serial.println(inputData);
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