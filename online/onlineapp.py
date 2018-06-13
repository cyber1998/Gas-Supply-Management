from flask import Flask, render_template, request
import MySQLdb
from onlinedb import InsertToMYSQLTable
app = Flask(__name__)

@app.route('/register', methods = ['GET', 'POST'])
def signup():
	if request.method == "POST":
		user = request.form['uname']
		password = request.form['pass']	
		email = request.form['email']
		if(user == None) or (password == None) or (email == None):#Needs Correction
			return render_template("loginpage.html", error="BLAH")
	
		print(user)
		print(password)
		print(email)
		try:
			InsertToMYSQLTable("Users",user, password, email)
		except:
			return("<h3> Error in Inserting </h3>")
	return(render_template("registered.html", title = "Registered"))	

@app.route('/home')
def index():
	return render_template("loginpage.html", title = "Login")

@app.route('/contact_us')
def contact():
	return render_template("contact.html", title = "Contact Us")

@app.route('/')
def landingpage():
	return render_template("loginpage.html", title = "Login")

@app.route('/about_us')
def aboutus():
	return render_template("about.html", title="About Us")

@app.route('/tariff')
def tariff():
	return render_template("tariff.html", title= "Tariffs")







if __name__ == "__main__":
	app.run("127.0.0.1", 5030, debug=True)

	