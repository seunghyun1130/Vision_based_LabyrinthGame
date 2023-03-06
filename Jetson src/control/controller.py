from common.customcrc16 import CRC16_CCITTFALSE
from common.config import one_step

previous_angle = [0,0] # global varible handling previous angle

#dummy
dummy_move = [0x02, 0x00, 0x01, 0x0A, 0xff, 0xff, 0xff, 0x03]

class MotorControl:
    def __init__(self):
        self.default = 0
        self.crcagent = CRC16_CCITTFALSE()
        
    def makeAngleInRange(self, preangle):
        # preangle extected in [-1, 0, 1]
        return_angle = []
        return_angle.append(previous_angle[0] + preangle[0]*one_step)  
        return_angle.append(previous_angle[1] + preangle[1]*one_step)        
        previous_angle[0] = return_angle[0]; previous_angle[1] = return_angle[1]
        
        return return_angle
        
    def move_servo_msg(self, bus, address, angle_array):
        angle = self.makeAngleInRange(angle_array)
        
        # for motor1
        dummy_move[4] = angle[0]
        crc_base = bytes(dummy_move[1:4])
        crc_h, crc_l = self.crcagent.makeCRC(crc_base)    
        dummy_move[-3] = crc_h; dummy_move[-2] = crc_l    
        
        ret = bus.write_byte(bytes(dummy_move))
        
        if not ret:
            return False 
        
        arduret = bus.read_byte(address)
        if not arduret:
            return False 
        
        return True


