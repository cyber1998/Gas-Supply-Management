from appJar import *
import MySQLdb


def showUsers():
	print("Showing Users")

def addUsers():
	print("Adding Users")

def delUsers():
	print("Deleting Users")


def close():
	app.stop()


def auth(button):
	username = app.getEntry("Username")
	password = app.getEntry("Password")
	db = MySQLdb.connect(host = "127.0.0.1", user =  "customer", passwd = "password", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		SELECT * FROM storeadmins_master;
		''')
	accounts = cursor.fetchall()
	for account in accounts:
		if username == account[1] and password == account[2]:
				print("Logged in")

def manageUsers(button):
	return

def userBills(button):
	return



# app = gui("Admin Interface", "640x480")
# app.addLabel("title", "Admin Interface")
# app.setBg('orange')
# app.setFont(18)
# app.addButtons(["Manage Users", "User Bills", "Cancel"], [manageUsers,userBills,close])
# app.startSubWindow("Login", modal = True)
# app.addLabel("login","Adminstrators Login")
# app.addLabelEntry("Username")
# app.addSecretEntry("Password")
# app.addButtons(["Submit","Close"], [auth, app.hideSubWindow("Login")])
# app.stopSubWindow(subWindow("login"))
# app.go()


app = gui()
app.addButtons(["one", "two"], launch)

app.startSubWindow("one", modal = True)
app.addLabel("l1", "SubWindow One")
app.stopSubWindow()

app.startSubWindow("two")
app.addLabel("l2", "SubWindow Two")
app.stopSubWindow()

app.go()