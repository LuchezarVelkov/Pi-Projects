#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

# Setup Raspberry Pi GPIO  numbering
GPIO.setmode(GPIO.BCM)    # Set GPIO to be at GPIO numbering
GPIO.setwarnings(False)   # Turn OFF warning to GPIO in use

touch = 25 # GPIO number of Touch Sensor !
green_led = 4 # GPIO number of GREEN LED !
red_led = 8 # GPIO number of RED LED !
yelow_led = 7 # GPIO number of Yellow LED !

#Setup GPIO Direction
GPIO.setup(touch, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(green_led, GPIO.OUT) # Set pin to be input !
GPIO.output(green_led, 0) # Set pin to be in low state !
GPIO.setup(red_led, GPIO.OUT) # Set pin to be input !
GPIO.output(red_led, 0) # Set pin to be in low state !
GPIO.setup(yelow_led, GPIO.OUT) # Set pin to be input !
GPIO.output(yelow_led, 0) # Set pin to be in low state !


#Create function blink.
def blink(pin):                          #  
        GPIO.output(pin,GPIO.HIGH)       #
        time.sleep(0.5)                  #
        GPIO.output(pin,GPIO.LOW)        #
        time.sleep(0.5)                  #
        return   

while True:
	try:
		time.sleep(1)
		if GPIO.input(touch) == 0:
			print('Finger Detected !')
		else:
			print('No Finger')

	except KeyboardInterrupt:
		GPIO.cleanup() 
		print "\n Program ended by user !"
		break
