#!/usr/bin/python
#
# Keyboard 4 x 4 driver
# Create by Luki 01.06.2017
# 

import RPi.GPIO as GPIO
import time
import os

k_pin1 = 17
k_pin2 = 18
k_pin3 = 19
k_pin4 = 20
k_pin5 = 21
k_pin6 = 22
k_pin7 = 23
k_pin8 = 24

GPIO.setmode (GPIO.BCM)
GPIO.setup(k_pin1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(k_pin2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(k_pin3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(k_pin4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(k_pin5, GPIO.OUT)
GPIO.output(k_pin5, 1)
GPIO.setup(k_pin6, GPIO.OUT)
GPIO.output(k_pin6, 1)
GPIO.setup(k_pin7, GPIO.OUT)
GPIO.output(k_pin7, 1)
GPIO.setup(k_pin8, GPIO.OUT)
GPIO.output(k_pin8, 1)

try:
    while True:
        time.sleep(0.3)                                  # Program wait 100ms
        if GPIO.input(k_pin4) == 1:                      # Keyboard COLUM (1) pressed
            GPIO.setup(k_pin4, GPIO.OUT)                 # Set keyboard pin 4 to be output
            GPIO.output(k_pin4, 1)                       # Set keyboard pin 4 to be HIGHT
            GPIO.setup(k_pin8, GPIO.IN, GPIO.PUD_DOWN)   # Set Keyboard pin 8 to be input in LOW state
            GPIO.setup(k_pin7, GPIO.IN, GPIO.PUD_DOWN)   # Set Keyboard pin 7 to be input in LOW state
            GPIO.setup(k_pin6, GPIO.IN, GPIO.PUD_DOWN)   # Set Keyboard pin 6 to be input in LOW state
            GPIO.setup(k_pin5, GPIO.IN, GPIO.PUD_DOWN)   # Set Keyboard pin 5 to be input in LOW state
            if GPIO.input(k_pin8) == 1:
                print '1'
            if GPIO.input(k_pin7) == 1:
                print '4'
            if GPIO.input(k_pin6) == 1:
                print '7'
            if GPIO.input(k_pin5) == 1:
                print '*'
            else:
                GPIO.setup(k_pin4, GPIO.IN, GPIO.PUD_DOWN)  
                GPIO.setup(k_pin8, GPIO.OUT)             
                GPIO.output(k_pin8, 1)                   
                GPIO.setup(k_pin7, GPIO.OUT)            
                GPIO.output(k_pin7, 1)                   
                GPIO.setup(k_pin6, GPIO.OUT)             
                GPIO.output(k_pin6, 1)                   
                GPIO.setup(k_pin5, GPIO.OUT)             
                GPIO.output(k_pin5, 1)                   
            
        if GPIO.input(k_pin3) == 1:                      # Keyboard COLUM (2) pressed
            GPIO.setup(k_pin3, GPIO.OUT)
            GPIO.output(k_pin3, 1)
            GPIO.setup(k_pin8, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin7, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin6, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin5, GPIO.IN, GPIO.PUD_DOWN)
            if GPIO.input(k_pin8) == 1:
                print '2'
            if GPIO.input(k_pin7) == 1:
                print '5'
            if GPIO.input(k_pin6) == 1:
                print '8'
            if GPIO.input(k_pin5) == 1:
                print '0'
            else:
                GPIO.setup(k_pin3, GPIO.IN, GPIO.PUD_DOWN)
                GPIO.setup(k_pin8, GPIO.OUT)
                GPIO.output(k_pin8, 1)
                GPIO.setup(k_pin7, GPIO.OUT)
                GPIO.output(k_pin7, 1)
                GPIO.setup(k_pin6, GPIO.OUT)
                GPIO.output(k_pin6, 1)
                GPIO.setup(k_pin5, GPIO.OUT)
                GPIO.output(k_pin5, 1)

        if GPIO.input(k_pin2) == 1:                      # Keyboard COLUM (3) pressed
            GPIO.setup(k_pin2, GPIO.OUT)
            GPIO.output(k_pin2, 1)
            GPIO.setup(k_pin8, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin7, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin6, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin5, GPIO.IN, GPIO.PUD_DOWN)
            if GPIO.input(k_pin8) == 1:
                print '3'
            if GPIO.input(k_pin7) == 1:
                print '6'
            if GPIO.input(k_pin6) == 1:
                print '9'
            if GPIO.input(k_pin5) == 1:
                print '#'
            else:
                GPIO.setup(k_pin2, GPIO.IN, GPIO.PUD_DOWN)
                GPIO.setup(k_pin8, GPIO.OUT)
                GPIO.output(k_pin8, 1)
                GPIO.setup(k_pin7, GPIO.OUT)
                GPIO.output(k_pin7, 1)
                GPIO.setup(k_pin6, GPIO.OUT)
                GPIO.output(k_pin6, 1)
                GPIO.setup(k_pin5, GPIO.OUT)
                GPIO.output(k_pin5, 1)

        if GPIO.input(k_pin1) == 1:                      # Keyboard COLUM (4) pressed
            GPIO.setup(k_pin1, GPIO.OUT)
            GPIO.output(k_pin1, 1)
            GPIO.setup(k_pin8, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin7, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin6, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.setup(k_pin5, GPIO.IN, GPIO.PUD_DOWN)
            if GPIO.input(k_pin8) == 1:
                print 'A'
            if GPIO.input(k_pin7) == 1:
                print 'B'
            if GPIO.input(k_pin6) == 1:
                print 'C'
            if GPIO.input(k_pin5) == 1:
                print 'D'
            else:
                GPIO.setup(k_pin1, GPIO.IN, GPIO.PUD_DOWN)
                GPIO.setup(k_pin8, GPIO.OUT)
                GPIO.output(k_pin8, 1)
                GPIO.setup(k_pin7, GPIO.OUT)
                GPIO.output(k_pin7, 1)
                GPIO.setup(k_pin6, GPIO.OUT)
                GPIO.output(k_pin6, 1)
                GPIO.setup(k_pin5, GPIO.OUT)
                GPIO.output(k_pin5, 1)


except KeyboardInterrupt:
    GPIO.cleanup()
