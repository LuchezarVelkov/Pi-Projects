#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess
import os
 
print 'Enter Hour'
Data = raw_input()
print "Enter Minutes"
Data2 = raw_input()
with open("text.txt", "r+") as fo:
	fo.seek(0, 0)
	fo.write(Data)
        fo.seek(0, 1)
	fo.write(Data2)
	fo.closed

