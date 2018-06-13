import MySQLdb
s = input("Query? : ")
db = MySQLdb.connect(host = "192.168.0.177", user = "cyber", passwd = "bca4500815", db = "Flaskdb", port = 5000)
cursor = db.cursor()
cursor.execute(s)
allrows = cursor.fetchall()
for eachrow in allrows:
	print(eachrow[0])
db.commit()

