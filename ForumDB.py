import sqlite3 as sql

class ForumDB:
	cur = None

	def __init__(self, forumName="test"):
		#db = sql.connect(forumName + ".db")
		db = sql.connect(":memory:")
		self.cur = db.cursor()
		self.createDB() # TODO: Fix overwriting
		print("ForumDB init...")

	def createDB(self):
		cur = self.cur
		cur.execute("CREATE TABLE users(id int AUTO_INCREMENT, name varchar, password varchar, level int)")
		cur.execute("CREATE TABLE topic(id int AUTO_INCREMENT, userid int, name varchar)")
		cur.execute("CREATE TABLE posts(id int AUTO_INCREMENT, userid int, topicid int, msg varchar)")

	def addUser(self, username, level="user"):
		cur = self.cur
		cur.execute("INSERT INTO users (name, level) VALUES (?, ?)", (username, level))

	def addTopic(self, userid, name):
		cur = self.cur
		cur.execute("INSERT INTO topic (userid, name) VALUES (?, ?)", (userid, name))

	def addPost(self, userid, topicid, msg):
		cur = self.cur
		cur.execute("INSERT INTO posts (userid, topicid, msg) VALUES (?, ?, ?)", (userid, topicid, msg))

	def getUsers(self):
		cur = self.cur
		cur.execute("SELECT name FROM users ORDER BY id")
		return cur.fetchall()

	def getTopics(self):
		cur = self.cur
		cur.execute("SELECT name FROM topic ORDER BY id")
		return cur.fetchall()

	def getPosts(self, topicid):
		cur = self.cur
		cur.execute("SELECT msg FROM posts WHERE topicid=? ORDER BY id", topicid)
		return cur.fetchall()
