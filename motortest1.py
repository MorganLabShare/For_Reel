#!/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
#~ import atexit
import sys

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

motor=int(sys.argv[1])
speed=int(sys.argv[2])
direction=sys.argv[3]

myMotor = mh.getMotor(motor)


if direction == "1":
	myMotor.run(Adafruit_MotorHAT.FORWARD)
elif direction == "2":
	myMotor.run(Adafruit_MotorHAT.BACKWARD)
else:
	print("The direction was not interpreted")
#~ myMotor.run(Adafruit_MotorHAT.RELEASE)

myMotor.setSpeed(speed)

time.sleep(2)

myMotor.run(Adafruit_MotorHAT.RELEASE)

turnOffMotors()
