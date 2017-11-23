#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 26 as BCM is soil moisture1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 0)
