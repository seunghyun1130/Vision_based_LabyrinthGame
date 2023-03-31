from common.customcrc16 import CRC16_CCITTFALSE
from common.config import motordc, dataframe
import smbus as sm # for dummy

previous_angle = [0,0] # global varible handling previous angle


class MotorControl:
    def __init__(self):
        self.default = 0
        self.crcagent = CRC16_CCITTFALSE()
        self.bus = sm.SMBus(2)
        
    def makeAngleInRange(self, preangle):
        # preangle extected in [-1, 0, 1]
        return_angle = []
        return_angle.append(previous_angle[0] + preangle[0]*motordc.one_step)  
        return_angle.append(previous_angle[1] + preangle[1]*motordc.one_step)    

        for i in range(2):
            if return_angle[i] < 0:
                return_angle[i] = 0

        previous_angle[0] = return_angle[0]; previous_angle[1] = return_angle[1]
        
        return return_angle
        
    def move_servo_msg(self,address, angle_array):
        angle = self.makeAngleInRange(angle_array)
        
        dataframe[2] = angle[0]; dataframe[3] = angle[1]
        crc_h, crc_l = self.crcagent.makeCRC(dataframe)    
        dataframe[-3] = crc_h; dataframe[-2] = crc_l    
        
        ret = self.bus.write_i2c_block_data(address, 0x02, dataframe)
        
        # return 값이 없는 듯 하여 여기는 주석처리
        # if not ret:
        #     return False 
        
        arduret = self.bus.read_byte(address) # should be sth like 7
        if not arduret:
            return False 
        
        return True



# if __name__=="__main__":
#     mc = MotorControl()
#     mc.move_servo_msg(address, [15,30])
