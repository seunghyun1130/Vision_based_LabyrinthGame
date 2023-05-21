#include <Wire.h>

int rcv = 0;
int rcv_stat = 0;
byte _rcvBuf[7];

void receiveEvent(int bytes) {
  int index = 0;
  rcv = Wire.read();
  _rcvBuf[0] = rcv;
  while(Wire.available()){
    rcv = Wire.read();
    _rcvBuf[++index] = rcv;
    rcv_stat += 1;
    // Serial.print("Receive Data : ");
    // Serial.println(rcv); 
  }

  for(int i = 0; i<7; i++){
   Serial.println(_rcvBuf[i]); 
  }

  // return ACK
  Wire.write(rcv_stat);
  rcv_stat = 0;
}

void sendData(){
    Wire.write(rcv); // 쓰는건 아닌데 살려는 두자
}

void i2c_setup()
{
  Wire.begin(Address);
  Wire.onReceive(receiveEvent);
//  Wire.onRequest(sendData);
}