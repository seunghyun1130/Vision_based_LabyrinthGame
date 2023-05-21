#include <HardwareSerial.h> //for rs485 comm
HardwareSerial rs485(2); // rxtx mode 2 of 0,1,2

#include "driver_const.h"
#include <string.h>
#include <math.h>

short recData1[12];
short recData2[12];
short trashBuffer[180];

short initBuffer[3][3];
short prevBuffer[3][3];
short newBuffer[3][3];
float diffBuffer[3][3];

/*
 * buffer structure
 **********************************************************************
 *           dev1[x] | dev1[y] | dev1[z] |
 *           -----------------------------
 *accel      |       |         |         |
 *           -----------------------------
 *angle      |       |         |         |
 *           -----------------------------
 *angularvel |       |         |         |
 *           -----------------------------
 ***********************************************************************
 */

static float accDiff[6];
static float angDiff[6];
static float angvelDiff[6];

int flag = 0;

void sendCommand(byte command[8], int prt){
  byte data[10];
  for(int i=0;i<8;i++){
    data[i]=command[i];
    }
  if(prt==1){
    for(int i = 0;i<8;i++){
      Serial.print(command[i],HEX);
      if(i != 7){
        Serial.print(",");
        }
      }
    }
  rs485.write(data, 8);
//  Serial.println();
  rs485.flush();
}


void calibrateAcc(){
      Serial.println("---------- Acceleration Calibration Init ----------");
      sendCommand(unlockMaster1,1);
      delay(500);
      sendCommand(accCalmode1,1);
      delay(6000);
      sendCommand(setNormal1,1);
      delay(1000);
      sendCommand(saveConfig1,1);
      delay(1000);
}
  
void calibrateMag(){
      Serial.println("---------- Magnetic Calibration Init ----------");
      sendCommand(unlockMaster1,1);
      delay(500);
      sendCommand(magCalmode1,1);
      Serial.println("---------- Slowly rotate in 3 axis ----------");
      delay(5000);
      Serial.println("---------- May stop now :) ----------");
      sendCommand(setNormal1,1);
      delay(1000);
      sendCommand(saveConfig1,1);
      delay(1000);  
}
  

int rs485_receive(short recv[], int num){
    unsigned long t = millis(); 
    while(1){
      if(millis() - t > 10000){
        return -1;
        break;
      }
      for (int i = 0; (rs485.available() > 0) && (i < num); i++) {
        recv[i] = rs485.read();
      }
      return 0;
      break;
    }
}
  
void readAcceleration(){
    sendCommand(readAcc1,0);
    if(rs485_receive(recData1, 11) != -1){
      /*
      for(int i = 0;i<11;i++){
        Serial.print(recData1[i],HEX);
        Serial.print(",");
        }
      */
        
      }
     else{
      Serial.println("no resp");
      Serial.println();    
      } 
    rs485.flush();
    delay(5);
}

void readSensorAngle(){
    sendCommand(readAngle1,0);
    if(rs485_receive(recData1, 11) != -1){
      /*
      for(int i = 0;i<11;i++){
        Serial.print(recData1[i],HEX);
        Serial.print(",");
        }
        */
      }
     else{
      Serial.println("no resp");
      Serial.println();    
      } 
    rs485.flush();
    delay(5);
}

void readAngularVelocity(){
    sendCommand(readAngVel1,0);
    if(rs485_receive(recData1, 11) != -1){
      
      for(int i = 0;i<11;i++){
        /*
        Serial.print(recData1[i],HEX);
        Serial.print(",");
        }
        
        */
      }}
     else{
      Serial.println("no resp");
      Serial.println();    
      } 
    rs485.flush();
    delay(5);
}

// device 1,2 // type 0,1,2
void savebuffer(short tarbuf[3][3], int type){
    tarbuf[type][0]=(((short)recData1[3]<<8)|recData1[4]);
    tarbuf[type][1]=(((short)recData1[5]<<8)|recData1[6]);
    tarbuf[type][2]=(((short)recData1[7]<<8)|recData1[8]);
}

void printAccel(short rec[]){
  short data_x = (((short)rec[3]<<8)|rec[4])/(32768/(16*9.81));
  short data_y = (((short)rec[5]<<8)|rec[6])/(32768/(16*9.81));
  short data_z = (((short)rec[7]<<8)|rec[8])/(32768/(16*9.81));
  Serial.print(data_x);Serial.print("   "); Serial.print(data_y);Serial.print("   ");Serial.println(data_z);
}

void printAngle(short rec[]){
  short data_x = (((short)rec[3]<<8)|rec[4])/(32768/180);
  short data_y = (((short)rec[5]<<8)|rec[6])/(32768/180);
  short data_z = (((short)rec[7]<<8)|rec[8])/(32768/180);
  Serial.print(data_x);Serial.print("   "); Serial.print(data_y);Serial.print("   "); Serial.println(data_z);
}

void printAngVel(short rec[]){
  short data_x = (((short)rec[3]<<8)|rec[4])/(32768/2000);
  short data_y = (((short)rec[5]<<8)|rec[6])/(32768/2000);
  short data_z = (((short)rec[7]<<8)|rec[8])/(32768/2000);
  Serial.print(data_x);Serial.print("   "); Serial.print(data_y);Serial.print("   "); Serial.println(data_z);
}
  
// type 0,1,2
void calculateVal(float arr[], int type){
  for(int i=0; i<3; i++){
    if(type==0){
        arr[i] = (newBuffer[type][i] - initBuffer[type][i])/(32768/(16*9.81));
      }
    else if(type==1){
        arr[i] = (newBuffer[type][i] - initBuffer[type][i])/(32768/180);
      }
    else if(type==2){
        arr[i] = (newBuffer[type][i] - initBuffer[type][i])/(32768/2000);
      }
    diffBuffer[type][i]=arr[i];
    }

    Serial.print(arr[0]);Serial.print("   "); Serial.print(arr[1]);Serial.print("   "); Serial.println(arr[2]);
}

float calcAbsVal(int type){
  float val;
  val = sqrt(pow(diffBuffer[type][0],2.0) + pow(diffBuffer[type][1],2.0) + pow(diffBuffer[type][2],2.0));  
  Serial.println(val);        
  return val;
}

void readSensor(short buf[3][3]){
  readAcceleration();
  savebuffer(buf, 0);
  readSensorAngle();
  savebuffer(buf, 1);
  readAngularVelocity();
  savebuffer(buf, 2);
}

void calcSensor(){
  calculateVal(accDiff, 1);
  calculateVal(angDiff, 1);
  calculateVal(angvelDiff, 1);
}

void clearBuffer(){
  for(int i=0; i<3;i++){
    for(int j=0; j<3;j++){
      prevBuffer[i][j] = newBuffer[i][j];
      newBuffer[i][j] = 0;
      }
  }
}



void setupWT32() 
{ 
  rs485.begin(9600, SERIAL_8N1);
  rs485.flush();


  Serial.println("--------------- Serial Initiated ---------------");
  calibrateAcc();
  calibrateMag();
  Serial.println("--------------- Calibration Done ---------------");
  rs485.flush();
  
  if(rs485_receive(trashBuffer, 180) != -1){
    for(int i = 0;i<180;i++){
      Serial.print(trashBuffer[i],HEX);
      Serial.print(",");
      }
      Serial.println();
  }
  Serial.println("--------------- Setup Done ---------------");
}


void gyro_loop() 
{ 
  rs485.flush();
  if(++flag==1){
    Serial.println("WT901C485 read");
    readSensor(initBuffer);
    for(int i = 0;i<3;i++){
      for(int j = 0; j<6;j++){
        Serial.print(initBuffer[i][j]);
        Serial.print("  ");       
        }
       Serial.println();
      }
    readSensor(prevBuffer);
    delay(500);
  }
  readSensor(newBuffer);
  calcSensor();
//   postHTTP(1);
  clearBuffer();
}