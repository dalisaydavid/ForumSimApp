import MySQLdb as sql

class ForumDB:
	cur = None

	def __init__(self, forumName="test"):
		#db = sql.connect(forumName + ".db")
		dbpw = raw_input("Enter SQL DB password: ")
		global db
		db = sql.connect("host214.hostmonster.com", "dalisayd_grognak", dbpw, "dalisayd_forumsimapp")
		db.autocommit(True)
		self.cur = db.cursor()
		print("ForumDB init...")

	def getCommands(self, userid):
		cur = self.cur
		cur.execute("SELECT * FROM commands")
		allCommands = cur.fetchall()
		cmdsAvail = []
		for cmd in allCommands:
			cur = db.cursor()
			cur.execute("SELECT %s FROM permissions WHERE userid=%s" % (cmd[1],userid))
			if cur.fetchone()[0] == 1:
				cmdsAvail.append(cmd)
		return cmdsAvail

	def addUser(self, username,pswd):
		cur = self.cur
		cur.execute("INSERT INTO users (id,name,password) VALUES (%s, %s, %s)", (None, username,pswd))

	def addTopic(self, userid, name):
		cur = self.cur
		cur.execute("INSERT INTO topic (userid, name) VALUES (%s, %s)", (userid, name))

	def addPost(self, userid, topicid, msg):
		cur = self.cur
		cur.execute("INSERT INTO posts (userid, topicid, msg) VALUES (%s, %s, %s)", (userid, topicid, msg))

	def getUsers(self):
		cur = self.cur
		cur.execute("SELECT id,name FROM users ORDER BY id")
		return cur.fetchall()

	def getUsersByUserPass(self, username, pswd):
		cur = self.cur
		cur.execute("SELECT id FROM users where name=%s AND password=%s", (username,pswd))
		return cur.fetchone()

	def getTopics(self):
		cur = self.cur
		cur.execute("SELECT id,name FROM topic ORDER BY id")
		return cur.fetchall()

	def getPosts(self, topicid):
		cur = self.cur
		cur.execute("SELECT id,msg FROM posts WHERE topicid=%s ORDER BY id", topicid)
		return cur.fetchall()

	def delTopic(self, topicid):
		cur = self.cur
		cur.execute("DELETE FROM topic WHERE id=%s", topicid)
		print "Topic Deleted."

	def delPost(self, postid):
		cur = self.cur
		cur.execute("DELETE FROM posts WHERE id=%s", postid)
		print "Post Deleted."

	def delUser(self, userid):
		cur = self.cur
		cur.execute("DELETE FROM users WHERE id=%s", userid)
		print "User Deleted."
	
	def authenticate(self, username, password):
		cur = self.cur
		try:
			cur.execute("SELECT password FROM users WHERE name=%s", username)
			userpw = cur.fetchone()[0]
		except:
			return -1

		if userpw is None or userpw != password:
			return -1

		cur.execute("SELECT id FROM users WHERE name=%s", username)
		userid = cur.fetchone()[0]
		return userid

	def hasPermission(self, userid, permission):
		cur = self.cur
		cur.execute("SELECT %s FROM permissions WHERE userid=%s" % (permission, userid))
		fetch = cur.fetchone()[0]
		return fetch

	def modifyPermissions(self, userid, permissions):
		cur = self.cur
		execute = "insert into permissions (userid"
		for p in permissions:
			execute += ", %s" % str(p)
		execute += ") values(%s" % str(userid[0])
		for i in range(len(permissions)):
			execute += ",1"
		execute += ")"
		print execute
		cur.execute(execute)	
	
        def isLegalCommand(self, cmd):
            cur = self.cur
            cur.execute("SELECT * FROM commands WHERE name=%s", (cmd))
            return (cur.rowcount > 0)
