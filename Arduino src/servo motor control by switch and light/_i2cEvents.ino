char receiveEvent(int bytes) {
  char inputData;
  inputData = Wire.read();
  Serial.print("Receive Data : ");
  Serial.println(inputData);

  return inputData;
}

void sendData(char ACK){
    Wire.write(ACK);
}