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
		return [,,modes[4]]								# auth() returns a list of the form [ID, Name, Session - True/False, Mode - Read/Set]
		
	elif id == AdminID:
		return [,,modes[5]]								# auth() returns a list of the form [ID, Name, Session - True/False, Mode - Read/Set]
		
	elif checkID(id):
		## Authentication stuff goes here
		
		print(keypad.SendLine(command["good"]))			# Sends "Correct" Code to Keypad
		time.sleep(2)
		print(keypad.SendLine(name))					# Sends Student Name to Keypad
		
		# beginning logging information
		
		return [,,modes[int(keypad.ReadLine())]]		# auth() returns a list of the form [ID, Name, Session - True/False, Mode - Read/Set]
	else:
		print(keypad.SendLine(command["wrong"]))		# Sends "Wrong" Code to Keypad
		time.sleep(2)
		return modes[0]	
	
