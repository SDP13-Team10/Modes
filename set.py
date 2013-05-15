import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from questionBank import QuestionBank

keypad = keypad()
motor = motors()

qBank = QuestionBank(databaseLocation)

def set():
	print(keypad.SendLine(modeLookUp["set"]))
	print(motor.SendLine(modeLookUp["set"]))
	time.sleep(2)
	#tme = currentTime.strftime("%H, %M")
	qBank.generateTime()
	senttime = setModeTime(id)
	print(keypad.SendLine(senttime))
	randomTime = qBank.getTimeTouple()
	speakTime(randomTime[0],randomTime[1])
	motortime = qBank.getTimeString()

	try:

		comm = COMMAND[str(keypad.read())]
	
		if comm == "GET_TIME":
			motortime = getTimeFromMotor()
	
		#else
		
		if senttime == motortime:
			print(keypad.SendLine(command["good"]))
			time.sleep(2)
			print(keypad.SendLine(modeLookUp["normal"]))
			print(motor.SendLine(modeLookUp["normal"]))
			return modes[0]
			
		else:
			print(keypad.SendLine(command["wrong"]))
			time.sleep(2)
			print(keypad.SendLine(modeLookUp["normal"]))
			print(motor.SendLine(modeLookUp["normal"]))
			return modes[0]

	except KeyError:
		print "Error!!!"
		return modes[0]
		
def setModeTime(ID):

	# Get difficulty level that the student is on
	# return time based on that level
	global qBank
	return qBank.getTimeString()
		