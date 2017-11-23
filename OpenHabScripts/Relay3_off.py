#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 19 as BCM is soil moisture1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, 1)
