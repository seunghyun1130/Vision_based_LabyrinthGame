
#dummy
dummy_move = [0x02, 0x00, 0x01, 0x01, 0xff, 0x03]

class MotorControl:
    def __init__(self):
        self.default = 0
    
    def move_servo_msg(self, bus, address, angle):
        dummy_move[4] = hex(angle)
        ret = bus.write_byte(bytes(dummy_move))
        if not ret:
            return False 
        
        arduret = bus.read_byte(address)
        if not arduret:
            return False 
        
        return True


