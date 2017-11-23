#!/usr/bin/python
import sys
import Adafruit_DHT

sensor = 11
pin = 12
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
     print('{0:0.1f}'.format(humidity))
else:
     print('Failed to get reading. Try again!')
     sys.exit(1)
