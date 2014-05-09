import Commands
def begin(uname,role):
	global isActive
	global introMessage
	global userName
	global forumRole
	userName = uname
	forumRole = role
	introMessage = "Welcome to the superawesome forums, %s!" % userName 
	isActive = True
	display(introMessage)
	run()


def run():
	while True:
		Commands.performCommand(cmd=getNextCommand(),userName=userName,level='forumLevel',role=forumRole)

def getNextCommand():
	global askNextCommandMessage 
	askNextCommandMessage = "What's your next action?\n"
	return raw_input(askNextCommandMessage)

	
# Dalisayd 3/29/14 - Made this a separate method just in case we have to parse specific strings
def display(msg):
	print msg
