def cmdCanPerformAction(db, userid, cmd):
	if not db.isLegalCommand(cmd):
		return -1
	elif not db.hasPermission(userid,cmd):
		return 0
	else:
		return 1	 

def cmdViewTopics(db, userid, index=0):
	topics = db.getTopics()
	topics = topics[index:]

	for topic in topics:
		print "%i) %s" % (topic[0], topic[1])

def cmdViewPosts(db,userid,topicId=None,index=0):
	if topicId == None:
		posts = db.getPosts()
	else:
		posts = db.getPosts(topicId)
	posts = posts[index:]
	for post in posts:
		print "%i) %s" % (post[0],post[1])

def cmdAddTopic(db, userid, topicName):
	db.addTopic(userid,topicName)

def cmdAddPost(db, userid, topicId, postMsg):
	db.addPost(userid,topicId, postMsg)
'''
def canGetCommand(level, cmd, role):
	if cmd not in commands[level] or not (cmd in adminPriv and role == 'admin'):  # if they are requested admin actions and are admin 
		return False
	return True

def performCommand(cmd, userName=None, level=None, role='member', db):
	if not canGetCommand(level, cmd, role):
		print "Command not permitted"
		return	
	elif cmd == "addUser":
		db.addUser(userName, level)

	elif cmd == "getUsers":
		users = db.getUsers()
		id = 1
		print "id:\tuser:"
		for user in users:
			print str(id) + "\t" + user[0]
			id += 1

def viewActions(level):
	print getAvailableActions(level)	
		
def getAvailableActions(level):
	availActions = ""
	for command in commands[level]:
		availActions.append(command + "\n")
	return availActions
'''
