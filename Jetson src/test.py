#! /usr/bin/python3
import smbus as sm

address = 0x50
bus = sm.SMBus(2)

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    data = 150

    writeNumber(data)
    number = readNumber()