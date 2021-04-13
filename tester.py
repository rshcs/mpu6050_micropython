import mpu
from time import sleep as delay

angle = mpu.Mpu()


while True:
    print(angle.read_data())
    delay(2)



