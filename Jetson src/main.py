#! /usr/bin/python3
import smbus as sm
from control.controller import MotorControl
from common.config import address

# async function?
def logic(address, bus, controller):
    ret = controller.move_servo_msg(address, bus, angle_array)
    
    # send again if fail
    if not ret:
        ret = controller.move_servo_msg(address, bus, angle_array)
        return True
    else:
        return True
    
def main(address, bus):
    logic(address, bus)
    return True

if __name__=="__main__":
    bus = sm.SMBus(1)
    mc = MotorControl()
    main(address, bus, mc)