
commands = {
	'forumLevel': ['viewActions','viewForumMembers','viewDiscussions']
}

def getCommand(level,cmd):
	if canGetCommand(level,cmd):
		performCommand(level, cmd)

def canGetCommand(level,cmd):
	return cmd in commands[level]

def performCommand(level,cmd):
	if level in 'forumLevel':
		if cmd in "viewActions":
			viewActions(level)

def viewActions(level):
	if level in 'forumLevel':
		print getAvailableActions(level)	
		
def getAvailableActions(level):
	availActions = ""
	if level in 'forumLevel':
		for command in commands[level]:
			availActions.append(command + "\n")
	return availActions
