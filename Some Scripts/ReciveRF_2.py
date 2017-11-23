#!/usr/bin/python
# RF 433 Mhz code read
# Create By Luki at 28.05.2017
import RPi.GPIO as GPIO, time, sys

GPIO.setmode(GPIO.BCM)

print ('Are you using GPIO 27 |yes| or |no| ?')
pinuse = raw_input()
if pinuse == 'yes':
  GPIO.setup(27, GPIO.IN)
  rf = 27
  print ('Please enter the vale of code (Defaulth 200):')
  maxcount = input()
else:
  print ('Enter GPIO what you use:')
  pinuse = int(raw_input())
  GPIO.setup(pinuse, GPIO.IN)
  print ('Please enter the vale of code (Defaulth 200):')
  maxcount = input()
  rf = pinuse

while True:
  pin = GPIO.input(rf)
  if pin:
    count = 0
    while (count < maxcount):
      pin = GPIO.input(rf)
      sys.stdout.write(str(int(pin)))
      pin = 0
      count = count + 1
      if count == maxcount:
        print("---")
