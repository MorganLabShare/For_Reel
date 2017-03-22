#!/bin/python

import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
timer=0
while timer < 20:
	time.sleep(0.2)
	print("pin 19: "+str(GPIO.input(19)))
	print("pin 13: "+str(GPIO.input(13)))
	print("pin 16: "+str(GPIO.input(16)))
	timer = timer+1

GPIO.cleanup()
