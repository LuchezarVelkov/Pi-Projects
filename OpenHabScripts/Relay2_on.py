#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 21 as BCM is soil moisture1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 0)
