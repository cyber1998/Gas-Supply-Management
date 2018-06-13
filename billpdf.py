#from pyPDF2 import *\
import MySQLdb

def calculate_price(city,units):
	if city == 'New Delhi':
		if units <= 30:
			return 5*units
		if units > 30 and units <= 50:
			return 8*units
		if units > 50 and units <= 80:
			return 10*units
		if units > 80 and units <= 100:
			return 12*units
		if units > 100:
			return 15*units
		#code
	if city == 'Kolkata':
		if units <= 30:
			return 4*units
		if units > 30 and units <= 50:
			return 7*units
		if units > 50 and units <= 80:
			return 9*units
		if units > 80 and units <= 100:
			return 12*units
		if units > 100:
			return 15*units
		#code
	if city == 'Mumbai':
		if units <= 30:
			return 8*units
		if units > 30 and units <= 50:
			return 9*units
		if units > 50 and units <= 80:
			return 10*units
		if units > 80 and units <= 100:
			return 13*units
		if units > 100:
			return 15*units
		#code
	if city == 'Ahmedabad':
		if units <= 30:
			return 6*units
		if units > 30 and units <= 50:
			return 7*units
		if units > 50 and units <= 80:
			return 9*units
		if units > 80 and units <= 100:
			return 12*units
		if units > 100:
			return 15*units
		#code
	if city == 'Bangalore':
		if units <= 30:
			return 7*units
		if units > 30 and units <= 50:
			return 9*units
		if units > 50 and units <= 80:
			return 10*units
		if units > 80 and units <= 100:
			return 12*units
		if units > 100:
			return 15*units
		#code



def fetchPrice(aadhar):
	db = MySQLdb.connect(host = "192.168.0.177", user =  "cyber", passwd = "bca4500815", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	query = "SELECT id, name, payable_amount FROM MasterTable WHERE id = %s;"
	cursor.execute(query, (aadhar,))
	row = cursor.fetchone()
	return row

def cusBillsUpdate(billid, payable_amount):
	db = MySQLdb.connect(host = "192.168.0.177", user =  "customer", passwd = "password", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		UPDATE MasterTable SET bill_id = %s, payable_amount = %s);
		''',(str(bill_id), payable_amount,))
	db.commit()
	print("Record for bills updated")
	return

def cusBillsInsert(billid, name, username, payable_amount):
	db = MySQLdb.connect(host = "192.168.0.177", user =  "customer", passwd = "password", db = "FlaskDB",port=5000)
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO CustomerBills(bill_id, name, username, payable_amount) VALUES (%s,%s,%s,%s);
		''',(str(bill_id), name, username, payable_amount,))
	db.commit()
	print("Record for bills Inserted")
	return



from datetime import datetime
def write_bill(aadharID):
	record = selectNameFromMasterTable(aadharID)
	#today = str(datetime.date.today())
	bill = "Bill_"+(aadharID)
	currentYear = datetime.now().year
	currentMonth = datetime.now().month
	filename = bill+"-"+str(currentYear)+"-"+str(currentMonth)+".doc"
	f = open(filename.strip(""), 'w')
	f.write("Customer Name : ", record[1])
	f.write("Customer ID : ", record[0])
	f.write("Bill for the month " + str(currentMonth) +"/" + str(currentYear)[:2])
	f.write("Bill = Rs.", record[2])
	f.write("Thank You")


write_bill("2515215215")
