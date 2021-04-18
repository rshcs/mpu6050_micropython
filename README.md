### mpu6050_micropython
---

- [x] X Y Z Accelerometer raw outputs  
- [x] X Y Z Gyro raw outputs
- [x] Temperature optput in celsius 
- [ ] Calibration
- [ ] Lean angle from gyro/ Accelerometer reading   
---  
   
Micropython Library for MPU6050 Gyro/Accelerometer module.  
- Tested with ESP8266 nodemcu.

---
#### Wiring
Seperate power supply (5v) or logic level converter (5 -3.3v) for NodeMCU is not required.
|NodeMCU|MPU6050(GY-521)|
|---|---|
|3.3v|Vcc|
|Gnd|Gnd|
|D1|SCL|
|D2|SDA|

