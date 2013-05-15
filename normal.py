#!/usr/bin/python	
# Normal Mode (Can be launched two ways: python normal.py or ./normal.py with permission)

import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from questionBank import QuestionBank


keypad = keypad()
motor = motors()

qBank = QuestionBank(databaseLocation)

def normal():
	print "in normal"
	comm = COMMAND[str(keypad.ReadLine())]		## use different method other than stuff dictionary
	print "recieved" 
	print comm
	if comm == "SPEAK_TIME":
		speakTime(nowHour(), nowMinute())
		print(keypad.write(modeLookUp["normal"]))
		keypad.flushInput()
		comm = ""
		print comm
		return modes[0]
	elif comm == "WAKE_UP":					## send check ID signal to keypad and motor
		print(keypad.SendLine(modeLookUp["check_id"]))
		print(motor.SendLine(modeLookUp["check_id"]))
			
		return modes[1]						## return statements???
	else:
		return modes[0]


		

