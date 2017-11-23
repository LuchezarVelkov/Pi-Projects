#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 5 as BCM is soil moisture3
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

if GPIO.input(5) == 1:
    print 1
else:
    print 0
GPIO.cleanup()
