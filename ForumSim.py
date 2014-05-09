import FSShell as shell
import Authenticator

userName = raw_input("User Name:")
role = Authenticator.authenticate(userName)
if role: # if role has something in it
	shell.begin(userName,role)
