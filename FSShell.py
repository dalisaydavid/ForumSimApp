import Commands as do
import sys

def begin(uid, db):
	global isActive
	global introMessage
	global userId
	userId = uid
	introMessage = "Welcome to the superawesome forums!"
	isActive = True
	display(introMessage)
	run(db)


def run(db):
	while True:
		#Commands.performCommand(cmd=getNextCommand(), userName=userName, level='forumLevel', role=forumRole, db=db)
		cmd = getNextCommand().lower()

		if do.cmdCanPerformAction(db,userId,cmd):
			if cmd == "viewtopics":
				do.cmdViewTopics(db, userId)
			elif cmd == "viewposts":
				if do.cmdCanPerformAction(db,userId,"viewtopics"):
					print "Select Topic:"
					do.cmdViewTopics(db,userId)
					topicSelection = raw_input("")
					do.cmdViewPosts(db,userId,topicSelection)			
			elif cmd == "quit" or cmd == "exit":
				sys.exit()
		else:
			print "Invalid privileges to perform this command."
def getNextCommand():
	global askNextCommandMessage 
	askNextCommandMessage = "What's your next action?\n"
	return raw_input(askNextCommandMessage)
	
# Dalisayd 3/29/14 - Made this a separate method just in case we have to parse specific strings
def display(msg):
	print msg
