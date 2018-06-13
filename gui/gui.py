from appJar import *

import MySQLdb


def modUsers():
	print("Showing Users")

def addUsers():
	app.showSubWindow("Create New User")
	print("Adding Users")

def delUsers():
	print("Deleting Users")


def close(win):
	app.hideSubWindow(win)


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

def submit():
	print("Submitting")
	return

def cancel():
	print("Cancelled")
	return

def launch(win):
	app.showSubWindow(win)


app = gui()
app.addButtons(["Manage Users", "User Bills"],launch)

app.startSubWindow("Manage Users", modal = True)
app.addLabel("l1", "User Management")
app.addButtons(["Create New User", "Delete a User", "Modify a User"], [addUsers, delUsers, modUsers])
app.stopSubWindow()

app.startSubWindow("User Bills")
app.addLabel("l2", "User Billing")
app.stopSubWindow()


app.startSubWindow("Create New User", modal = True)
app.addLabel("u1", "New Customer:")
app.addLabelEntry("Aadhar ID:")
app.addLabelEntry("Name:")
app.addLabelEntry("Address")
app.addLabelOptionBox("City:", ["New Delhi", "Mumbai", "Ahemedabad", "Bangalore", "Kolkata"])
app.addLabelEntry("Email:")
app.addLabelEntry("Password:")
app.addLabelEntry("Desired Username:")
app.addButtons(["Submit","Cancel"], [submit, cancel])
app.stopSubWindow()


app.go()