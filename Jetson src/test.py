#! /usr/bin/python3
import smbus as sm
import time
from common.customcrc16 import CRC16_CCITTFALSE

address = 0x50
bus = sm.SMBus(2)
crcagent = CRC16_CCITTFALSE()

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

def testData(angle1, angle2):
    dataframe = [0x07, 0xff, 0xff, 0xff, 0xff, 0x03]
    dataframe[2] = angle1; dataframe[3] = angle2
    crc_h, crc_l = crcagent.makeCRC(dataframe)    
    dataframe[-3] = crc_h; dataframe[-2] = crc_l  
    
    ret = bus.write_i2c_block_data(address, 0x02,dataframe)
    
    return dataframe

while True:
    number = readNumber()
    data = testData(15, 30)
    print(data)
    time.sleep(5)
    data = testData(45, 10)
    print(data)
    time.sleep(5)