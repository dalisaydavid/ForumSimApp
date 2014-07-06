import FSShell as shell
import ForumDB as fdb

db = fdb.ForumDB()
role = -1

while role is -1:
	username = raw_input("User Name: ")
	password = raw_input("Password: ")
	role = fdb.authenticate(username, password)

	if role is -1:
		print "\nInvalid username or password.\n"

shell.begin(userName,role)