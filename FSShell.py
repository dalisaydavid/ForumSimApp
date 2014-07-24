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
		if cmd == "quit" or cmd == "exit":
			sys.exit()
		if do.cmdCanPerformAction(db,userId,cmd) == 1:
			if cmd == "help":
				do.getCommands(db,userId)
			elif cmd == "viewtopics":
				do.cmdViewTopics(db, userId)
			elif cmd == "viewposts":
				if do.cmdCanPerformAction(db,userId,"viewtopics"):
					print "Select Topic:"
					do.cmdViewTopics(db,userId)
					topicSelection = raw_input("")
					do.cmdViewPosts(db,userId,topicSelection)
			elif cmd == "viewusers":
				do.cmdViewUsers(db,userId)
			elif cmd == "adduser":
				newUserName = raw_input("New Username:")
				newUserPswd = raw_input("New User password:")
				newUserId = do.cmdAddUser(db,newUserName,newUserPswd)
				newPermisIn = raw_input("What permissions should {0} have? (separate my commas)".format(newUserName))
				newPermisList = newPermisIn.split(",")
				do.cmdModifyPermissions(db,newUserId,newPermisList)
			elif cmd == "addtopic":
				topicName = raw_input("Name of new topic: ")
				if raw_input("Create topic %s?" % topicName).lower() == "y":
					do.cmdAddTopic(db,userId,topicName)		
			elif cmd == "addpost":
				print "Select Topic:"
				do.cmdViewTopics(db,userId)
				topicSelection = raw_input("")
				do.cmdAddPost(db,userId,int(topicSelection),raw_input("Post Body: "))
			elif cmd == "deletetopic":
				print "Select Topic to remove:"
				do.cmdViewTopics(db,userId)
				topicSelection = raw_input("")
				do.cmdDeleteTopic(db,userId,int(topicSelection))
			elif cmd == "deletepost":
				print "Select Topic:"
				do.cmdViewTopics(db,userId)
				topicSelection = raw_input("")
				print "Select Post to remove:"
				do.cmdViewPosts(db,userId,topicSelection)
				postSelection = raw_input("")
				do.cmdDeletePost(db, userId, postSelection)
			elif cmd == "deleteuser":
				print "Select User:"
				do.cmdViewUsers(db,userId)
				userSelection = raw_input("")
				do.cmdDeleteUser(db,userSelection)
		elif do.cmdCanPerformAction(db,userId,cmd) == -1:
			print "Command not found."
		else:
			print "Invalid privileges to perform this command."
def getNextCommand():
	global askNextCommandMessage 
	askNextCommandMessage = "What's your next action?\n"
	return raw_input(askNextCommandMessage)
	
# Dalisayd 3/29/14 - Made this a separate method just in case we have to parse specific strings
def display(msg):
	print msg
