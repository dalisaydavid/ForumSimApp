# dalisayd - Commands.py used for anything command dependent
import sys
from ForumDB import ForumDB

db = ForumDB()

commands = {
	'forumLevel': ['viewActions','viewForumMembers','viewDiscussions']
}

def getCommand(level, cmd):
	if canGetCommand(level, cmd):
		performCommand(level, cmd)

def canGetCommand(level, cmd):
	return cmd in commands[level]

def performCommand(cmd,userName=None,level=None):
	if cmd == "adduser":
		db.addUser(userName,level)

	elif cmd == "getusers":
		users = db.getUsers()
		id = 1

		print "id:\tuser:"
		for user in users:
			print str(id) + "\t" + user[0]
			id += 1

	else:
		print "Unknown command"

def viewActions(level):
	print getAvailableActions(level)	
		
def getAvailableActions(level):
	availActions = ""
	for command in commands[level]:
		availActions.append(command + "\n")
	return availActions
