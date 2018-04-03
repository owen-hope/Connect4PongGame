import RPi.GPIO as GPIO
from neopixle import *

LED_COUNT = 42 # Number of LED pixels in strand
LED_PIN = 19 # GPIO pin connected tot he pixles (must support PWM).
LED_FREQ_HZ = 800000 # LED siginal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating siginal
LED_INVERT = False # True to invert the siginal (when using NPN transistor level shift)

player1 = ''
player2 = ''

# The x,y values that each IR sensor controls
IR0 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
IR1 = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]
IR2 = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)]
IR3 = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
IR4 = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)]
IR5 = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
IR6 = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT) # IR light
GPIO.setup(17, GPIO.IN) # IR reader

boardValues = {}
countEven = 0
countOdd = 11

#size of connect 4 board
x = 7
y = 6

# Dictionary with key:(x,y) and value [value of light on/off, nameOfPlayer, light value]
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

# Testing of break for IR light
if GPIO.input(17) == 0:
    print("There was a break")

while True:
    lightOn(17, IR0, boardValues)


#need at end to reset status of GPIO pins
GPIO.cleanup()

#################################
# All functions below this point

# Checks for break in IR beam.
#turns light on and changes value in Dictionary
def lightOn(gpioPin, IRSensor, matrix):
    beamBreak = False
    if GPIO.input(gpioPin) == 0:
        print("There was a break")
        beamBreak = True
        for x in range(IRSensor):
            value = matrix[x]
            if value[0] == 0:
                value[0] == 1

                return
            else:
                continue
