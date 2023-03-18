from common.customcrc16 import CRC16_CCITTFALSE
from common.config import one_step, dataframe

import smbus as sm # for dummy

previous_angle = [0,0] # global varible handling previous angle


class MotorControl:
    def __init__(self):
        self.default = 0
        self.crcagent = CRC16_CCITTFALSE()
        
    def makeAngleInRange(self, preangle):
        # preangle extected in [-1, 0, 1]
        return_angle = []
        return_angle.append(previous_angle[0] + preangle[0]*one_step)  
        return_angle.append(previous_angle[1] + preangle[1]*one_step)    

        for i in range(2):
            if return_angle[i] < 0:
                return_angle[i] = 0

        previous_angle[0] = return_angle[0]; previous_angle[1] = return_angle[1]
        
        return return_angle
        
    def move_servo_msg(self,address, bus, angle_array):
        angle = self.makeAngleInRange(angle_array)
        
        dataframe[2] = angle[0]; dataframe[3] = angle[1]
        crc_h, crc_l = self.crcagent.makeCRC(dataframe)    
        dataframe[-3] = crc_h; dataframe[-2] = crc_l    
        
        ret = bus.write_byte(address, bytes(dataframe))
        
        if not ret:
            return False 
        
        arduret = bus.read_byte(address)
        if not arduret:
            return False 
        
        return True

    def move_servo_msg_dummy(self):    
        dataframe[2] = 15; dataframe[3] = 30
        crc_h, crc_l = self.crcagent.makeCRC(dataframe)    
        dataframe[-3] = crc_h; dataframe[-2] = crc_l    

        print(dataframe)
        
        # ret = bus.write_byte(address, bytes(dataframe))
        
        if not ret:
            return False 
        
        # arduret = bus.read_byte(address)
        # if not arduret:
        #     return False 
        
        return True


if __name__=="__main__":
    mc = MotorControl()
    mc.move_servo_msg_dummy()
