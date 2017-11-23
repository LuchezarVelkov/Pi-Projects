#!/usr/bin/python
#
import RPi.GPIO as GPIO
import time
import os
import lcddriver
from time import *

lcd = lcddriver.lcd()
print 'Welcome to RSI'
print 'Version:   1.0'
lcd.lcd_display_string("Welcome to RSI", 1)
lcd.lcd_display_string("Version:   1.0", 2)
sleep(5)
lcd.lcd_clear()
lcd.lcd_display_string("Do you use Z 1 ?", 1)
lcd.lcd_display_string("1-Yes   |   2-No", 2)
print 'Do you use zone 1 |y| or |n|'
Z1_use = raw_input()
if Z1_use == "y":
        print 'Please enter zone 1 name:'
        lcd.lcd_clear()
        lcd.lcd_display_string("Please enter", 1)
        lcd.lcd_display_string("zone 1 name:", 2)
        Z1 = raw_input()
        print 'Do you use zone 2 |y| or |n|'
        lcd.lcd_clear()
        lcd.lcd_display_string("Do you use", 1)
        lcd.lcd_display_string("zone 2 Y / N ?", 2)
        Z2_use = raw_input()
else:
        print 'Do you use zone 2 |y| or |n|'
        lcd.lcd_clear()
        lcd.lcd_display_string("Do you use", 1)
        lcd.lcd_display_string("zone 2 Y / N ?", 2)
        Z2_use = raw_input()
if Z2_use == "y":
        print 'Please enter zone 2 name:'
        lcd.lcd_clear()
        lcd.lcd_display_string("Please enter", 1)
        lcd.lcd_display_string("zone 2 name:", 2)
        Z2 = raw_input()
        print 'Do you use zone 3 |y| or |n|'
        lcd.lcd_clear()
        lcd.lcd_display_string("Do you use zone", 1)
        lcd.lcd_display_string("zone 3 |Y||N| ?", 2)
        Z3_use = raw_input()
else:
        print 'Do you use zone 3 |y| or |n|'
        Z3_use = raw_input()
if Z3_use == "y":
        print 'Please enter zone 3 name:'
        Z3 = raw_input()
        print 'Do you use zone 4 |y| or |n|'
        Z4_use = raw_input()
else:
        print 'Do you use zone 4 |y| or |n|'
        Z4_use = raw_input()
if Z4_use == "y":
        print 'Please enter zone 4 name:'
        Z4 = raw_input()
        print 'Do you use zone 5 |y| or |n|'
        Z5_use = raw_input()
else:
        print 'Do you use zone 5 |y| or |n|'
        Z5_use = raw_input()
if Z5_use == "y":
        print 'Please enter zone 5 name:'
        Z5 = raw_input()
        print 'Do you use zone 6 |y| or |n|'
        Z6_use = raw_input()
else:
        print 'Do you use zone 6 |y| or |n|'
        Z6_use = raw_input()
if Z6_use == "y":
        print 'Please enter zone 6 name:'
        Z6 = raw_input()
        print 'Do you use zone 7 |y| or |n|'
        Z7_use = raw_input()
else:
        print 'Do you use zone 7 |y| or |n|'
        Z7_use = raw_input()
if Z7_use == "y":
        print 'Please enter zone 7 name:'
        Z7 = raw_input()
        print 'Do you use zone 8 |y| or |n|'
        Z8_use = raw_input()
else:
        print 'Do you use zone 8 |y| or |n|'
        Z8_use = raw_input()
if Z8_use == "y":
        print 'Please enter zone 8 name:'
        Z8 = raw_input()
os.system("clear")
        
zone1 = 16
zone2 = 18
#zone3 = 0
#zone4 = 0
#zone5 = 0
#zone6 = 0
#zone7 = 0
#zone8 = 0
led = 13

previous_state1 = False
current_state1 = False
previous_state2 = False
current_state2 = False
previous_state3 = False
current_state3 = False
previous_state4 = False
current_state4 = False
previous_state5 = False
current_state5 = False
previous_state6 = False
current_state6 = False
previous_state7 = False
current_state7 = False
previous_state8 = False
current_state8 = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(zone1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(zone2, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(zone3, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(zone4, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(zone5, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(zone6, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(zone7, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(zone8, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)
print 'Press Ctrl + C  to Quit monitoring.'
try:
        while True:
                sleep(0.1)
                if Z1_use == 'y': #Zone_1
                        previous_state1 = current_state1
                        current_state1 = GPIO.input(zone1)
                        if current_state1 != previous_state1:
                                new_state1 = "HIGH" if current_state1 else "LOW"
                                if new_state1 == "HIGH":
                                        print('Zone '+ Z1 + ' Open at '+ (strftime("%X %x")))
                                        
                                        GPIO.output(led, 1)
                                        sleep(5)
                                elif new_state1 == "LOW":
                                        print('Zone '+ Z1 + ' Close at '+ (strftime("%X %x")))
                                        GPIO.output(led, 0)
                                        sleep(5)

                if Z2_use == 'y': #Zone_2
                        previous_state2 = current_state2
                        current_state2 = GPIO.input(zone2)
                        if current_state2 != previous_state2:
                                new_state2 = "HIGH" if current_state2 else "LOW"
                                if new_state2 == "HIGH":
                                        print('Zone '+ Z2 + ' Open at '+ (strftime("%X %x")))
                                        GPIO.output(led, 1)
                                        sleep(5)
                                elif new_state2 == "LOW":
                                        print('Zone '+ Z2 + ' Close at '+ (strftime("%X %x")))
                                        GPIO.output(led, 0)
                                        sleep(5)

                if Z3_use == 'y': #Zone_3
                        previous_state3 = current_state3
                        current_state3 = GPIO.input(zone3)
                        if current_state3 != previous_state3:
                                new_state3 = "HIGH" if current_state3 else "LOW"
                                if new_state3 == "HIGH":
                                        print('Zone '+ Z3 + ' Open at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 1)
                                        sleep(1)
                                elif new_state3 == "LOW":
                                        print('Zone '+ Z3 + ' Close at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 0)
                                        sleep(1)

                if Z4_use == 'y': #Zone_4               
                        previous_state4 = current_state4
                        current_state4 = GPIO.input(zone4)
                        if current_state4 != previous_state4:
                                new_state4 = "HIGH" if current_state4 else "LOW"
                                if new_state4 == "HIGH":
                                        print('Zone '+ Z4 + ' Open at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 1)
                                        sleep(1)
                                elif new_state4 == "LOW":
                                        print('Zone '+ Z4 + ' Close at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 0)
                                        sleep(1)
                                        
                if Z5_use == 'y': #Zone_5
                        previous_state5 = current_state5
                        current_state5 = GPIO.input(zone5)
                        if current_state5 != previous_state5:
                                new_state5 = "HIGH" if current_state5 else "LOW"
                                if new_state5 == "HIGH":
                                        print('Zone '+ Z5 + ' Open at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 1)
                                        sleep(1)
                                elif new_state5 == "LOW":
                                        print('Zone '+ Z5 + ' Close at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 0)
                                        sleep(1)

                if Z6_use == 'y': #Zone_6
                        previous_state6 = current_state6
                        current_state6 = GPIO.input(zone6)
                        if current_state6 != previous_state6:
                                new_state6 = "HIGH" if current_state6 else "LOW"
                                if new_state6 == "HIGH":
                                        print('Zone '+ Z6 + ' Open at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 1)
                                        sleep(1)
                                elif new_state6 == "LOW":
                                        print('Zone '+ Z3 + ' Close at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 0)
                                        sleep(1)

                if Z7_use == 'y': #Zone_7
                        previous_state7 = current_state7
                        current_state7 = GPIO.input(zone7)
                        if current_state7 != previous_state7:
                                new_state7 = "HIGH" if current_state2 else "LOW"
                                if new_state7 == "HIGH":
                                        print('Zone '+ Z7 + ' Open at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 1)
                                        sleep(1)
                                elif new_state7 == "LOW":
                                        print('Zone '+ Z7 + ' Close at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 0)
                                        sleep(1)
                                        
                if Z8_use == 'y': #Zone_8
                        previous_state8 = current_state8
                        current_state8 = GPIO.input(zone8)
                        if current_state8 != previous_state8:
                                new_state8 = "HIGH" if current_state8 else "LOW"
                                if new_state8 == "HIGH":
                                        print('Zone '+ Z8 + ' Open at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 1)
                                        sleep(1)
                                elif new_state8 == "LOW":
                                        print('Zone '+ Z8 + ' Close at '+ (time.strftime("%X %x")))
                                        GPIO.output(led, 0)
                                        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
