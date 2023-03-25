#include <Wire.h>

int rcv = 0;
const int Address = 0x50;
byte _rcvBuf[7];

void receiveEvent(int bytes) {
  int index = 0;
  rcv = Wire.read();
  _rcvBuf[0] = rcv;
  while(Wire.available()){
    rcv = Wire.read();
    _rcvBuf[++index] = rcv;
    Serial.print("Receive Data : ");
    Serial.println(rcv); 
  }

  for(int i = 0; i<8; i++){
   Serial.println(_rcvBuf[i]); 
  }
}

void sendData(){
    Wire.write(rcv); // 쓰는건 아닌데 살려는 두자
}

void setup()
{
  Serial.begin(115200);
  Wire.begin(Address);
  Wire.onReceive(receiveEvent);
//  Wire.onRequest(sendData);
}

void loop()
{
//    Serial.println("running...");
}
