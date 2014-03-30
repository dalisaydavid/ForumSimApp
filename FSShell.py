
def begin(userName="Anonymous User"):
	global isActive
	global introMessage
	introMessage = "Welcome to the Bray-Dalisay Forums, %s!" % userName 
	isActive = True
	display(introMessage)
	run()


def run():
	while True:
		getNextCommand()

def getNextCommand():
	global askNextCommandMessage 
	askNextCommandMessage = "What's your next action?\n"
	return raw_input(askNextCommandMessage)

	
# Dalisayd 3/29/14 - Made this a separate method just in case we have to parse specific strings
def display(msg):
	print msg
		
	
