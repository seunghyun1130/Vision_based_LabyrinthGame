#! /usr/bin/python3
import smbus as sm
import time
from common.customcrc16 import CRC16_CCITTFALSE

address = 0x50
bus = sm.SMBus(1)
crcagent = CRC16_CCITTFALSE()

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    print(number)
    return number

def testData():
    dataframe = [0x02, 0x07, 0xff, 0xff, 0xff, 0xff, 0x03]
    dataframe[2] = 15; dataframe[3] = 30
    crc_h, crc_l = crcagent.makeCRC(dataframe)    
    dataframe[-3] = crc_h; dataframe[-2] = crc_l    
    for i in range(len(dataframe)):
        ret = bus.write_byte(address, dataframe[i])
    return dataframe

while True:
    data = 100
    print(data)

    writeNumber(data)
    number = readNumber()
    data = testData()
    
    print(data)
    time.sleep(1)