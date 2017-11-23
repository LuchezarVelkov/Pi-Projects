#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 13 as BCM is rain sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)

if GPIO.input(13) == 1:
    print 1
else:
    print 0
GPIO.cleanup()
