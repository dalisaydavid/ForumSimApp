import FSShell as shell
import ForumDB as fdb

db = fdb.ForumDB()
userid = -1

while userid is -1:
	username = raw_input("User Name: ")
	password = raw_input("Password: ")
	userid = db.authenticate(username, password)

	if userid is -1:
		print "\nInvalid username or password.\n"

#print "Starting with uid: %s" % (userid)
shell.begin(userid, db)