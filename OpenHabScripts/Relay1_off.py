#!/usr/bin/python
import os
import commands
import RPi.GPIO as GPIO 

# Pin 20 as BCM is soil moisture1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, 1)