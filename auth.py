import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from questionBank import QuestionBank
from keypad import *
from Motors import *


keypad = keypad()
motor = motors()

def auth():

	TeacherID = 01475963
	AdminID = 36957410

	id = keypad.ReadLine()
	
	if id == TeacherID:
		return modes[4]
		
	elif id == AdminID:
		return modes[5]
		
	elif checkID(id):
		
		print(keypad.SendLine(command["good"]))			## Sends "Correct" Code to Keypad
		time.sleep(2)
		print(keypad.SendLine(name))			## Sends Student Name to Keypad
		
		# beginning logging information
		
		return modes[int(keypad.read())]		## return statements???
	else:
		print(keypad.SendLine(command["wrong"]))			## Sends "Correct" Code to Keypad
		time.sleep(2)
		return modes[0]	
	
