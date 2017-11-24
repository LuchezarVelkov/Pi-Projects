#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################
#             |Fingerprint R307 Manage Menu|             #
#                                                        #
#  Start date of project is                              #
#                           09.10.2017                   #
#                                      Create by Luki    #
##########################################################

import time
import tempfile
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

print 'What you want to do ?'
print 'For Index of FingerPrints press: [1]'
print 'For Search FingerPrint press: [2]'
print 'For Adding FingerPrint press: [3]'
print 'For Deleting FingerPrint press: [4]'
print 'For Download Image of FingerPrint press: [5]'

choice = raw_input()

if choice == '1': #Index of FingerPrints
    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to show a template index table page
    try:
        page = input('Please enter the index page (0, 1, 2, 3) you want to see: ')
        page = int(page)

        tableIndex = f.getTemplateIndex(page)

        for i in range(0, len(tableIndex)):
            print('Template at position #' + str(i) + ' is used: ' + str(tableIndex[i]))

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

if choice == '2': #Search FingerPrint
    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to search the finger and calculate hash
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            print('No match found!')
            exit(0)
        else:
            print('Found template at position #' + str(positionNumber))
            print("Welcome User:" + str(positionNumber) + " accsses acepted !")
            print('The accuracy score is: ' + str(accuracyScore))

        ## OPTIONAL stuff
        ##

        ## Loads the found template to charbuffer 1
        f.loadTemplate(positionNumber, 0x01)

        ## Downloads the characteristics of template loaded in charbuffer 1
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

        ## Hashes characteristics of template
        print('SHA-256 hash of template: ' + hashlib.sha256(characterics).hexdigest())

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

if choice == '3': #Adding FingerPrint
    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to enroll new finger
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Checks if finger is already enrolled
        result = f.searchTemplate()
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
            exit(0)

        print('Remove finger...')
        time.sleep(2)

        print('Waiting for same finger again...')

        ## Wait that finger is read again
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 2
        f.convertImage(0x02)

        ## Compares the charbuffers
        if ( f.compareCharacteristics() == 0 ):
            raise Exception('Fingers do not match')

        ## Creates a template
        f.createTemplate()

        ## Saves template at new position number
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

if choice == '4': #Deleting FingerPrint
    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to delete the template of the finger
    try:
        positionNumber = input('Please enter the template position you want to delete: ')
        positionNumber = int(positionNumber)

        if ( f.deleteTemplate(positionNumber) == True ):
            print('Template deleted!')

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

if choice == '5': #Download Image of FingerPrint
    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to read image and download it
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        print('Downloading image (this take a while)...')

        imageDestination =  '/home/pi/FingerPrint/Download_Image' + '/fingerprint.bmp'
        #imageDestination =  tempfile.gettempdir() + '/fingerprint.bmp'   ### Default to /temp/fingerprint.bmp
        f.downloadImage(imageDestination)

        print('The image was saved to "' + imageDestination + '".')

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
