#!/usr/bin/python 
import time
import lcddriver

from time import *

lcd = lcddriver.lcd()

while True:
    lcd.lcd_clear() # Clear the preview text in all rows
    lcd.backlight(1) # Turn On the backlight of display
    lcd.lcd_display_string("Welcome to", 1) # Print this mesage in first row
    lcd.lcd_display_string("Raspberry PI 3", 2) # Print this mesage in second row
    sleep(5) # wait 5 second to next command
    lcd.lcd_clear()
    lcd.lcd_display_string("Raspberry PI 3", 1)
    lcd.lcd_display_string("Model B", 2)
    sleep(3)
    lcd.lcd_clear()
    lcd.lcd_display_string("Model B", 1)
    lcd.lcd_display_string("This is LCD", 2)
    sleep(3)
    lcd.lcd_clear()
    lcd.lcd_display_string("This is LCD", 1)
    lcd.lcd_display_string("test program...", 2)
    sleep(3)
    lcd.lcd_clear()
    lcd.lcd_display_string("test program...", 1)
    sleep(3)
    lcd.backlight(0) # Turn Off the backlight of display
    sleep(3)
