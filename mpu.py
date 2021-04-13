
from machine import Pin, I2C
from time import sleep as delay

class Mpu:
    def __init__(self, i2c_addr = 104):
        self.i2c_addr = i2c_addr
        self.PWR_MNG_REG = 107
        self.STARTING_REG = 59

        self.i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

        self.i2c.writeto_mem(self.i2c_addr, self.PWR_MNG_REG, b'\x00') # PWR_MNG_REG value = 0
        delay(1) 

        self.mpu_raw = [0, 0, 0, 0, 0, 0, 0]

    def twos_comp(self, inV):
        intVal = int.from_bytes(inV, 'big')# bytearray to integer
        if intVal > 32767: # If it's negative
            return intVal - 65535 # 2's Comp
        else:
            return intVal
    
    def combine_bytes(self, inb):
        for x in range(len(inb) / 2): 
            self.mpu_raw[x] = self.twos_comp(inb[2*x: 2*x+2]) # 2's compliment
    
    def temperature(self):
        outV = (self.mpu_raw[3] / 340.00) + 36.53
        return outV 
    
    def read_data(self):
        in_bytes = self.i2c.readfrom_mem(self.i2c_addr, self.STARTING_REG, 14)
        self.combine_bytes(in_bytes) # Combine all 7 pair of bytes
        
        return self.mpu_raw[0:3] + [self.temperature()] + self.mpu_raw[4:7]


if __name__ == '__main__':
    angle = Mpu()

    while True:
        print(angle.read_data())
        delay(1)
    
