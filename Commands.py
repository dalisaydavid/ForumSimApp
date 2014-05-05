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

def performCommand(level, cmd):
	args = cmd.split(' ')

	if args[0] == "adduser":
		db.addUser(args[1], args[2])

	elif args[0] == "getusers":
		users = db.getUsers()
		id = 1

		print "id:\tuser:"
		for user in users:
			print str(id) + "\t" + user[0]
			id += 1

	else:
		print "Unknown command"

def viewActions(level):
	if level in 'forumLevel':
		print getAvailableActions(level)	
		
def getAvailableActions(level):
	availActions = ""
	if level in 'forumLevel':
		for command in commands[level]:
			availActions.append(command + "\n")
	return availActions
