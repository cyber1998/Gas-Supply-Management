from appJar import *
from creation import *
import MySQLdb


def modUsers():
	app.showSubWindow("Update a user", hide = False)

def addUsers():
	app.showSubWindow("Create New User", hide = False)


def auth(button):
	username = app.getEntry("lunm")
	password = app.getEntry("lpwd")
	if((username == "") and (password == "")):
		app.errorBox("Error", "Please enter a valid username and password to login")
		return
	if(username == ""):
		app.errorBox("Error", "Please enter a valid username")
		return
	if(password == ""):
		app.errorBox("Error", "Please enter a valid password")
		return
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		SELECT * FROM storeadmins_master;
		''')
	accounts = cursor.fetchall()
	for account in accounts:
		if username == account[1] and password == account[2]:
			app.show()
			return
	app.errorBox("Error", "Invalid Username and Password")
	return

def userBills(button):
	return

def submitNewCustomer():
	aadhar = app.getEntry("ncid")
	name = app.getEntry("ncnm")
	address = app.getEntry("ncad")
	city = app.getOptionBox("ncct")
	email = app.getEntry("ncem")
	password = app.getEntry("ncpw")
	user = app.getEntry("ncunm")
	users = selectAllFromMasterTable(aadhar)
	if users == None:
		try:
			adminMainInsert(aadhar, user, password, email, name, address, city)
			adminuserInsert(user, password, email)
			admincusdetInsert(aadhar, email, user, password, name, address, city)
			print("Adding User")
			return
		except:
			app.errorBox("Error", "Error during insertion to database. Please recheck.", parent = None)
			return
	app.errorBox("Error", "User already exists")
	return	

def modifyACustomer(btn):
	if btn == "updtserbtn":
		aadhar = app.getEntry("usearch")
		users = selectAllFromMasterTable(aadhar)
		if users == None:
			app.errorBox("Error","User not found", parent = None)
			return
		aadhar = app.setEntry("ucid", str(users[0]) , callFunction = True)
		name = app.setEntry("ucnm", str(users[4]) , callFunction = True)
		address = app.setEntry("ucad", str(users[5]) , callFunction = True)
		city = app.setOptionBox("ucct", str(users[6]) , callFunction = True)
		email = app.setEntry("ucem", str(users[3]), callFunction = True)
		password = app.setSecretEntry("ucpw", str(users[2]) , callFunction = True)
		user = app.setEntry("ucunm", str(users[1]),callFunction = True)

	if btn == "updtsubbtn":
		aadhar = app.getEntry("ucid")
		name = app.getEntry("ucnm")
		address = app.getEntry("ucad")
		city = app.getOptionBox("ucct")
		email = app.getEntry("ucem")
		password = app.getEntry("ucpw")
		user = app.getEntry("ucunm")
		try:
			adminMainUpdate(email, user, password, name, address, city, aadhar)
			adminCusDetUpdate(email, user, password, name, address, city, aadhar)
			adminUsersUpdate(email, user, password)
		except:
			app.errorBox("Error", "Error during updation. Please recheck.", parent = None)

	if btn == "updtdelbtn":
 		aadhar = app.getEntry("ucid")
 		try:
 			DeleteUser(aadhar)
 			app.infoBox("Success", "USER "+aadhar+" has been deleted.", parent = None)
 		except:
 			app.errorBox("Error", "Error during deleting.", parent = None)
	return


def launch(button):
	if button == "Manage Users":
		app.showSubWindow("Manage all Users")
	if button == "Users Bills":
		app.showSubWindow("User Bills")
	if button == "About":
		app.infoBox("About", "This software was written by the students of BIT Mesra, Kolkata Campus.\n Credits: Pooja Kumari\n Cyber Naskar\n Rakesh Kr. Mahto\n Manisha Singh", parent = None)


app = gui("PNG Supply Management System v1.0")
app.setFont(16)
app.addButtons(["Manage Users", "Users Bills", "About"], launch)

app.startSubWindow("Manage all Users", modal = True)
app.addLabel("main1", "User Management")
app.addButtons(["New User", "Modify a User"], [addUsers, modUsers])
app.addNamedButton("Close", "Manage all Users", app.hideSubWindow)
app.stopSubWindow()

app.startSubWindow("User Bills")
app.addLabel("main2", "User Billing")
app.addNamedButton("Close", "User Bills", app.hideSubWindow)
app.stopSubWindow()


app.startSubWindow("Create New User", modal = True)
app.addLabel("n", "New Customer:")
app.addLabel("nc1","Aadhar ID:")
app.addEntry("ncid")
app.setEntryMaxLength("ncid", 12)
app.addLabel("nc2","Name:")
app.addEntry("ncnm")
app.addLabel("nc3","Address:")
app.addEntry("ncad")
app.addLabel("nc4","City:")
app.addOptionBox("ncct", ["New Delhi", "Mumbai", "Ahemedabad", "Bangalore", "Kolkata"])
app.addLabel("nc5","Email:")
app.addEntry("ncem")
app.addLabel("nc6","Password:")
app.addSecretEntry("ncpw")
app.addLabel("nc7","Desired Username:")
app.addEntry("ncunm")
app.addNamedButton("Submit","newsubbtn", submitNewCustomer)

app.addNamedButton("Close", "Create New User", app.hideSubWindow)
app.stopSubWindow()


app.startSubWindow("Update a user")
app.addLabel("u", "Update Details")
app.addLabel("uc0", "Search User:")
app.addEntry("usearch")
app.setEntryMaxLength("usearch", 12)
app.addNamedButton("Search User", "updtserbtn", modifyACustomer)
app.addNamedButton("Delete User", "updtdelbtn", modifyACustomer)
app.addLabel("uc1","Aadhar ID:")
app.addEntry("ucid")
app.setEntryMaxLength("ucid", 12)
app.addLabel("uc2","Name:")
app.addEntry("ucnm")
app.addLabel("uc3","Address")
app.addEntry("ucad")
app.addLabel("uc4","City")
app.addOptionBox("ucct", ["New Delhi", "Mumbai", "Ahemedabad", "Bangalore", "Kolkata"])
app.addLabel("uc5","Email:")
app.addEntry("ucem")
app.addLabel("uc6", "Password:")
app.addEntry("ucpw")
app.addLabel("uc7","Desired Username:")
app.addEntry("ucunm")
app.addNamedButton("Submit","updtsubbtn", modifyACustomer)
app.addNamedButton("Close", "Update a user", app.hideSubWindow)
app.stopSubWindow()


app.startSubWindow("Login")
app.addLabel("login", "Admin Login")
app.addLabel("la1","Username")
app.addEntry("lunm")
app.addLabel("la2", "Password")
app.addSecretEntry("lpwd")
app.addNamedButton("Login","adminlogin", auth)
app.addNamedButton("Close", "Login", app.stop)
app.stopSubWindow()




app.go(startWindow = "Login")