#! /usr/bin/python3
import smbus as sm
from control.controller import MotorControl
from common.customcrc16 import CRC16_CCITTFALSE

address = 0x50
bus = sm.SMBus(1)
mc = MotorControl()

def logic(address, bus):
    
    return 0
    
def main():
    logic(address, bus)
    return

if __name__=="__main__":
    main()