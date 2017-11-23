#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import library for fingerprint reader
import os
import time
import RPi.GPIO as GPIO
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

# Import Library

from config import config  # Import functionality at config file.

# Import lcd functions
#lcd = lcddriver.lcd()

# import files
status_file = config["Luki_FingerPrint"] + "/Status/status_file.txt"     # Set location of file

# Setup Raspberry Pi GPIO  numbering
GPIO.setmode(GPIO.BCM)    # Set GPIO to be at GPIO numbering
GPIO.setwarnings(False)   # Turn OFF warning to GPIO in use

touch = 25      # GPIO number of Touch Sensor !
green_led = 4   # GPIO number of GREEN LED !
red_led = 8     # GPIO number of RED LED !
yelow_led = 7   # GPIO number of Yellow LED !

#Setup GPIO Direction
GPIO.setup(touch, GPIO.IN)      # GPIO.setup(touch, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(green_led, GPIO.OUT) # Set pin to be input !
GPIO.output(green_led, 0)       # Set pin to be in low state !
GPIO.setup(red_led, GPIO.OUT)   # Set pin to be input !
GPIO.output(red_led, 0)         # Set pin to be in low state !
GPIO.setup(yelow_led, GPIO.OUT) # Set pin to be input !
GPIO.output(yelow_led, 0)       # Set pin to be in low state !

#Create function blink.
def blink(pin):                          # Create function named blink 
        GPIO.output(pin,GPIO.HIGH)       #
        time.sleep(0.5)                  #
        GPIO.output(pin,GPIO.LOW)        #
        time.sleep(0.5)                  #
        return     

## Tries to initialize the sensor
try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity())) # Print current used template status

## Tries to search the finger and calculate hash
while True:
        try:
                if GPIO.input(touch) == 0: # if reader is touched rund srcipt
                        
                        print('Reading ...')

                        ## Wait that finger is read
                        while ( f.readImage() == False ):
                                pass

                        ## Converts read image to characteristics and stores it in charbuffer 1
                        f.convertImage(0x01)

                        ## Searchs template
                        result = f.searchTemplate()
                        #print 'Result = ' + str(result) ### Show Result          ###!!!###_T_E_S_T_I_N_G_###!!!###
                        positionNumber = result[0] # For positinNumber get first result
                        accuracyScore = result[1] # For accuracyScore get second result

                        if ( positionNumber == -1 ): # -1 is not recognised
                                os.system('mpg321 lock.mp3 -q')   # Play song if not recognised
                                print('No match found!')
                                for i in range(0,4):               # How times to blink 
                                        blink(red_led)             # What led to blink
                                time.sleep(1)                      # Add sleep time of 1 sec.
                                #exit(0)
                        else:                      # Anu number betwen 0-1000 is indexed.
                                os.system('mpg321 unlock.mp3 -q')  # Play song when recognised
                                print('\n' + 'Found template at position #' + str(positionNumber))    # Print finded position number
                                print('\n' + config['user_' + str(positionNumber)] + ' with accuracy score: ' + str(accuracyScore) + '\n')  # Print Name of user and accuracy of match
                                #print('The accuracy score is: ' + str(accuracyScore) + '\n')
                                for i in range(0,8):               # How times to blink 
                                        blink(green_led)           # What led to blink
                                #time.sleep(2)

                else:
                        time.sleep(0.01)  # Adding sleep time  if you dont add this time get cpu 100% usage bug
                        
        except KeyboardInterrupt:   # Except Ctrl + C comand to stop program
                GPIO.cleanup()      # Clear GPIO and restore it to default
                print "\n Program ended by user !"
                break               # Exit the program
        #except Exception as e:
                #print('Operation failed!')
                #print('Exception message: ' + str(e))
                #exit(1)
