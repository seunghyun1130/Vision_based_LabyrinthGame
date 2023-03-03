#! /usr/bin/python3
import smbus as sm
from control.controller import MotorControl
from common.customcrc16 import CRC16_CCITTFALSE

address = 0x50
bus = sm.SMBus(1)
mc = MotorControl()

def logic(data, address, bus):
    # I expect input to be an array [dir, ang]
    mc.move_servo_msg(bus, address, data[1])
    
def main(data, address, bus):
    logic(data, address, bus)
    return

if __name__=="__main__":
    main()