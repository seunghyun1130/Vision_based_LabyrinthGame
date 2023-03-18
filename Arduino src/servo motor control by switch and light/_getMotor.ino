int getMotor1() {
    int myList[] = {1, 2, 3, 4, 5};
    int listSize = sizeof(myList) / sizeof(int);
    int *ptr1 = myList + 1;
   
    //Serial.print(*ptr);
    
    return myList[1];
  }


int getMotor2() {
    int myList[] = {1, 2, 3, 4, 5};
    int listSize = sizeof(myList) / sizeof(int);
    int *ptr2 = myList + 2;

    return myList[2];
  }