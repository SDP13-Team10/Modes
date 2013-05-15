#!/usr/bin/python	
# Normal Mode (Can be launched two ways: python normal.py or ./normal.py with permission)

import time	# Does not execute this command when launched from terminal

greeting = "Welcome to ClockAide!"
mode = "Normal Mode"

def normal():
 print greeting
 print mode
 clock = time.ctime()
 print clock

def main():
 normal()

main()
# Include display to LCD Screen
# Include wait loop for keypad input


