#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 17 as BCM is soil moisture1
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

if GPIO.input(17) == 1:
    print 1
else:
    print 0
GPIO.cleanup()
