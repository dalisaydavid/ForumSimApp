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

	'''
	def createDB(self):
		cur = self.cur
		cur.execute("CREATE TABLE users(id int AUTO_INCREMENT, name varchar, password varchar, level int)")
		cur.execute("CREATE TABLE topic(id int AUTO_INCREMENT, userid int, name varchar)")
		cur.execute("CREATE TABLE posts(id int AUTO_INCREMENT, userid int, topicid int, msg varchar)")
	'''

	def addUser(self, username, level="user"):
		cur = self.cur
		cur.execute("INSERT INTO users (name, level) VALUES (%s, %s)", (username, level))

	def addTopic(self, userid, name):
		cur = self.cur
		cur.execute("INSERT INTO topic (userid, name) VALUES (%s, %s)", (userid, name))
	def addPost(self, userid, topicid, msg):
		cur = self.cur
		cur.execute("INSERT INTO posts (userid, topicid, msg) VALUES (%s, %s, %s)", (userid, topicid, msg))
	def getUsers(self):
		cur = self.cur
		cur.execute("SELECT name FROM users ORDER BY id")
		return cur.fetchall()

	def getTopics(self):
		cur = self.cur
		cur.execute("SELECT id,name FROM topic ORDER BY id")
		return cur.fetchall()

	def getPosts(self, topicid):
		cur = self.cur
		cur.execute("SELECT id,msg FROM posts WHERE topicid=%s ORDER BY id", topicid)
		return cur.fetchall()

	def authenticate(self, username, password):
		cur = self.cur
		cur.execute("SELECT password FROM users WHERE name=%s", username)
		userpw = cur.fetchone()[0]

		if userpw is None or userpw != password:
			return -1

		cur.execute("SELECT id FROM users WHERE name=%s", username)
		userid = cur.fetchone()[0]
		return userid

	def hasPermission(self, userid, permission):
		cur = self.cur
		cur.execute("SELECT %s FROM permissions WHERE userid=%s", (permission, userid))
		return cur.fetchone()[0]

	def isLegalCommand(self,cmd):
		cur = self.cur
		cur.execute("SELECT * FROM commands WHERE name=%s", (cmd))
		exists = 0
		for command in cur:
			if exists == 1:
				break
			exists += 1
		if exists == 0:
			return False	
		else:
			return True
