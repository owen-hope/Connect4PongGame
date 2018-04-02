import RPi.GPIO as GPIO
from neopixle import *

LED_COUNT = 42 # Number of LED pixels in strand
LED_PIN = 19 # GPIO pin connected tot he pixles (must support PWM).
LED_FREQ_HZ = 800000 # LED siginal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating siginal
LED_INVERT = False # True to invert the siginal (when using NPN transistor level shift)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

boardValues = {}
countEven = 0
countOdd = 11

#size of connect 4 board
x = 7
y = 6

# Dictionary with key:(x,y)
for i in range(x):
    for s in range(y):
        if i == 0 or i % 2 == 0:
            d[(i, s)] = [0, '', countEven]
            countEven = countEven + 1
        else:
            d[(i, s)] = [0, '', countOdd]
            countOdd = countOdd - 1
    if i % 2 == 0:
        countEven = countEven + 6
    elif i == 0:
        continue
    else:
        countOdd = countOdd + 18

if GPIO.input(17) == 0:
    print("There was a break")



#need at end to reset status of GPIO pins
GPIO.cleanup()
