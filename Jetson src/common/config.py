from dataclasses import dataclass

# controller
@dataclass
class motordc:
    motor_1 : int = 0xA0
    motor_2 : int = 0xA1
    one_step : int = 15

# CRC
@dataclass
class crcdc:
    POLYNOMIAL : int = 0x1021
    PRESET : int = 0xFFFF

# I2C
address = 0x50

# data frame
#           [stx, len, angle1, angle2, crc_h, crc_l, etx]
dataframe = [0x02, 0x07, 0xff, 0xff, 0xff, 0xff, 0x03]
