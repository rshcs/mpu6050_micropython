import math
import mpu
from time import sleep as delay

raw_value = mpu.Mpu()

def constrain(inv, minv, maxv):
    if inv < minv:
        return minv
    elif inv > maxv:
        return maxv
    else:
        return inv

while True:
    xaxis = raw_value.read_data()[0]
    yaxis = raw_value.read_data()[1]
    zaxis = raw_value.read_data()[2]
    #print(yaxis, xaxis, zaxis)
    rad_angle = math.atan2(xaxis , yaxis)
    print(math.degrees(rad_angle)+2.5)
    delay(.1)



