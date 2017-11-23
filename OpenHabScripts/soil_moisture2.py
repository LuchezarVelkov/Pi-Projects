#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 27 as BCM is soil moisture2
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

if GPIO.input(27) == 1:
    print 1
else:
    print 0
GPIO.cleanup()
