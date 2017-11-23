#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 6 as BCM is soil moisture4
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)

if GPIO.input(6) == 1:
    print 1
else:
    print 0
GPIO.cleanup()
