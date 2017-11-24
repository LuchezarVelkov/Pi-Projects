#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess
import os


with open("text.txt", "r") as fo: # If file is not at the same directory, write full path !
	fo.seek(0, 0) 
	hour = fo.read(2) # Read first four symbols
	fo.seek(0,1)
	minutes = fo.read(2)
	fo.closed
print hour + ":" +  minutes # Print what data is read.
