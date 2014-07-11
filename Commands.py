import ForumDB as fdb

# TODO

def cmdViewTopics(userid, index=0):
	if fdb.hasPermission(userid, "viewTopics"):
		topics = fdb.getTopics()
		topics = topics[index:index+10]

		for topic in topics:
			index += 1
			print "%i) %s" % (index, topic)

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