def cmdCanPerformAction(db, userid, cmd):
	if cmd == 'help':
		return 1
	if not db.isLegalCommand(cmd):
		return -1
	else:
		return  db.hasPermission(userid,cmd)

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

def cmdViewUsers(db, userid, index=0):
	users = db.getUsers()
	print "Users: "
	for user in users:
		print "{0}) {1}".format(user[0],user[1])

def cmdAddUser(db, userName, userPswd):
	db.addUser(userName,userPswd)
	id = db.getUsersByUserPass(userName, userPswd)
	return id			
def cmdModifyPermissions(db, userid, permissions):
	db.modifyPermissions(userid, permissions)	

def cmdAddTopic(db, userid, topicName):
	db.addTopic(userid,topicName)

def cmdAddPost(db, userid, topicId, postMsg):
	db.addPost(userid,topicId, postMsg)

def cmdDeleteTopic(db, userid, topicId):
	#db.delTopic(topicId)
	posts = db.getPosts(topicId)
	postIds = [post[0] for post in posts]
	for i in postIds:
		db.delPost(i)
	db.delTopic(topicId)
def cmdDeletePost(db, userid, postId):
	db.delPost(postId)

def cmdDeleteUser(db, userid):
	db.delUser(userid)
	
def getCommands(db, userid):
	cmds = db.getCommands(userid)
	print "Available commands:"
	for cmd in cmds:
		print "> {0}".format(cmd[1])
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
