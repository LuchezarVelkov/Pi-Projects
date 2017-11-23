#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 17 as BCM is soil moisture
soil_moisture = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(soil_moisture, GPIO.OUT)

if soil_moisture >= 1:
    print "Dry"
else:
    print "Wet"
GPIO.cleanup()

