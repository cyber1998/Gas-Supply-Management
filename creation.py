import MySQLdb

##INSERTIONS##
def adminMainInsert(aadhar, username, password, email, name, address, city, connectionid):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO MasterTable(id, username, password, email, name, address, city, connection_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
		''',(int(aadhar), username, password, email, name, address, city, connectionid,))
	db.commit()
	print("Record Updated")
	return


def adminuserInsert(username, password, email):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO Users(username, password, email) VALUES (%s,%s,%s);
		''',(username, password, email,))
	db.commit()
	print("Record Inserted")
	return

def admincusdetInsert(aadhar, email, username, password, name, address, city):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO CustomerDetails(id, email, username, password, name, address, city) VALUES (%s,%s,%s,%s,%s,%s,%s);
		''',(int(aadhar), email, username, password, name, address, city,))
	db.commit()
	print("Record Inserted")
	return


def customerMainInsert(aadhar, username, password, email, name, address, city, connectionid):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "customer", passwd = "password", db = "FlaskDB",port=5000)
	
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO MasterTable(id, username, password, email, name, address, city, connection_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
		''',(int(aadhar), username, password, email, name, address, city, connectionid,))
	db.commit()
	print("Record Inserted")
	return

def userInsert(username, password, email):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "customer", passwd = "password", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO Users(username, password, email) VALUES (%s,%s,%s);
		''',(username, password, email,))
	db.commit()
	print("Record Inserted")
	return

def cusdetInsert(aadhar, email, username, password, name, address, city):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "customer", passwd = "password", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO CustomerDetails(id, email, username, password, name, address, city) VALUES (%s,%s,%s,%s,%s,%s,%s);
		''',(int(aadhar), email, username, password, name, address, city,))
	db.commit()
	print("Record Inserted")
	return

# def cusBillsInsert(billid, name, username, payable_amount):
# 	db = MySQLdb.connect(host = "127.0.0.1", user =  "customer", passwd = "password", db = "FlaskDB",port=5000)
# 	cursor = db.cursor()
# 	cursor.execute('''
# 		INSERT INTO CustomerBills(bill_id, name, username, payable_amount) VALUES (%s,%s,%s,%s);
# 		''',(str(bill_id), name, username, payable_amount,))
# 	db.commit()
# 	print("Record for bills Inserted")
# 	return


##UPDATIONS##
def adminMainUpdate(email, username, password, name, address, city, aadhar):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		UPDATE MasterTable SET email = %s, username = %s, password = %s, name = %s, address = %s, city = %s WHERE id = %s;
		''',(email, username, password, name, address, city, int(aadhar),))
	db.commit()
	print("Record Inserted")
	return


def adminUsersUpdate(email, username, password):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		UPDATE Users SET email = %s, password = %s WHERE username = %s;
		''',(email, password, username))
	db.commit()
	print("Record Inserted")
	return

def adminCusDetUpdate(email, username, password, name, address, city, aadhar):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		UPDATE CustomerDetails SET username = %s, password = %s, name = %s, address = %s, city = %s WHERE email = %s;
		''',(username, password, name, address, city, email))
	db.commit()
	print("Record Inserted")
	return








##SELECTIONS##
def selectAllFromMasterTable(aadhar):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	query = "SELECT * FROM MasterTable WHERE id = %s;"
	cursor.execute(query, (aadhar,))
	row = cursor.fetchone()
	return row















##DELETIONS##
def DeleteUser(aadhar):
	db = MySQLdb.connect(host = "127.0.0.1", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''DELETE FROM mastertable WHERE id = %s;''', (int(aadhar),))
	print("User:"+aadhar+"was deleted")
	db.commit()
	return




