#! /usr/bin/python3
import smbus as sm

address = 0x50
bus = sm.SMBus(1)

def sendData(value):
    bus.write_byte(address, value)
    return -1

def readData():
    number = bus.read_byte(address)
    return number

if __name__=="__main__":
    while True:
        data = 225
        sendData(data)
        number = readData()

