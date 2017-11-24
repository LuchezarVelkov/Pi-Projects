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

print('What user number you wont to show ?')
positionNumber = raw_input()
 
print('\n' + config['user_' + str(positionNumber)])
