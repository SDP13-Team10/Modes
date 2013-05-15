import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from questionBank import QuestionBank

keypad = keypad()
motor = motors()

qBank = QuestionBank(databaseLocation)

def read():
	keypad.SendLine(modeLookUp["read"])
	motor.SendLine(modeLookUp["read"])
	time.sleep(2)
	qBank.generateTime()
	print(motor.write(readModeTime(id)))		## send time to be displayed to motor
	randomTime = qBank.getTimeTouple()
	#speakTime(randomTime[0],randomTime[1])
	readTime = keypad.read(5)			## include some timeout logic

# Check time entered for correctness and send appropriate signal.
# Create a readtime function

	if checkReadTime(readTime,qBank.getTimeString()):
		print(keypad.write(command["good"]))
		time.sleep(2)
		print(keypad.write(modeLookUp["normal"]))
		print(motor.write(modeLookUp["normal"]))
		return modes[0]
	else:
		print(keypad.write(command["wrong"]))
		time.sleep(2)
		print(keypad.write(modeLookUp["normal"]))
		print(motor.write(modeLookUp["normal"]))
		return modes[0]
		
def readModeTime(ID):
	
	# Get difficulty level that the student is on
	# return time based on that level
	
	global qBank
	return qBank.getTimeString()
	
def checkReadTime(readTime, sentTime):

	#Remove leading whitespaces:

	readTime = re.sub("^0+","",readTime)
	sentTime = re.sub("^0+","",sentTime)

	#Convert To Integers
	readHour = int(readTime.split(',')[0])
	readMinute = int(readTime.split(',')[1])

	sentHour = int(sentTime.split(',')[0])
	sentMinute = int(sentTime.split(',')[1])

	print "Check readTime entered"
	print "Time received: " + str(readHour) + "," + str(readMinute)
	print "Time sent: " + str(sentHour) + "," + str(sentMinute)
	# compare entered time with time given to student
	# return TRUE or False
	
	if readHour == sentHour and readMinute == sentMinute:
		return True
		
	else: 
		return False
	
	#return True

