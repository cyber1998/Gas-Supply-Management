import MySQLdb


def InsertToMYSQLTable(username,password,email):
	db = MySQLdb.connect(host = "db4free.net", user =  "cyberbit", passwd = "bca4500815", db = "flaskdbcyber",port=3306)
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO Users(username, password, email) VALUES (%s,%s,%s);''',(username, password,email,))
	db.commit()
	print("Record Inserted")
	return

def SelectUsersFromMYSQLTable():
	db = MySQLdb.connect(host = "db4free.net", user =  "cyberbit", passwd = "bca4500815", db = "flaskdbcyber",port=3306)
	cursor = db.cursor()
	cursor.execute('''SELECT * FROM Users;''')
	allrows = cursor.fetchall()
	for eachrow in allrows:
		print('{0}				{1}					{2}				{3}						'.format(eachrow[0], eachrow[1], eachrow[2], eachrow[3]))
	print("\nRecords Fetched")
	return



def DeleteUsersFromMYSQLTable(username):
	db = MySQLdb.connect(host = "db4free.net", user =  "cyberbit", passwd = "bca4500815", db = "flaskdbcyber",port=3306)
	cursor = db.cursor()
	cursor.execute('''DELETE FROM Users WHERE username = %s;''', (username,))
	print("User:"+username+"was deleted")
	db.commit()
	return

def CreateTable():
	db = MySQLdb.connect(host = "db4free.net", user =  "cyberbit", passwd = "bca4500815", db = "flaskdbcyber",port=3306)
	cursor = db.cursor()
	cursor.execute('''CREATE TABLE Users(
	id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
	username varchar(30) NOT NULL UNIQUE,
	password varchar(40) NOT NULL,
	email varchar(50) NOT NULL UNIQUE);''')
	print("Users Table Created")
	db.commit()
	return

def DescribeTable():
	db = MySQLdb.connect(host = "db4free.net", user =  "cyberbit", passwd = "bca4500815", db = "flaskdbcyber",port=3306)
	cursor = db.cursor()
	cursor.execute('''DESCRIBE Users;''')
	allrows = cursor.fetchall()
	for eachrow in allrows:
		print(eachrow)
	return




