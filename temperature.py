import time
import busio
import board
import adafruit_amg88xx
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

while 0.0 in amg.pixels[0]:
    pass
else:
    print(max(amg.pixels[0]))
