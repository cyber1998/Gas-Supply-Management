from flask import Flask, render_template, request, session, redirect, g, url_for
from datetime import *
#from werkzeug.security import generate_password_hash, check_password_hash
import os
import MySQLdb
from creation import *
app = Flask(__name__)


@app.route('/signup/register', methods=['GET', 'POST'])
def success():
    if session:
        session.pop("username", None)

    if request.method == "POST":
        user = request.form['uname'].strip("")
        password = request.form['pass']
        email = request.form['email']
        name = request.form['cus_name']
        address = request.form['addr']
        city = request.form['city']
        aadhar = request.form['aadhar']
        connectionid = aadhar+str(datetime.now().second) + \
            str(datetime.now().year)
        print(connectionid)
        if len(aadhar) < 12 or not aadhar.isdigit():
            return render_template("signup.html", error="Invalid AADHAR Number.")
        checkuser = selectAllFromMasterTable(aadhar)
        print(checkuser)
        if checkuser:
            return render_template("signup.html", error="This user already exists.")

        try:
            customerMainInsert(aadhar, user, password, email,
                               name, address, city, connectionid)
            userInsert(user, password, email)
            cusdetInsert(aadhar, email, user, password, name, address, city)
        except:
            return render_template("signup.html", error="Error during signup. Please try again after sometime.")
    return(render_template("registered.html", title="Registered"))


@app.route('/signup', methods=['GET', 'POST'])
def index():
    if g.username:
        return redirect(url_for("userpage", user=session['username']))
    return render_template("signup.html", title="Login")


@app.route('/')
@app.route('/home')
def intro():
    return render_template("intro.html", title="Home")


@app.route('/contact_us')
def contact():
    return render_template("contact.html", title="Contact Us")


@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/about_us')
def aboutus():
    return render_template("about.html", title="About Us")


@app.route('/tariff')
def tariff():
    return render_template("tariff.html", title="Tariffs")


@app.route('/changedetails')
def details():
    return render_template("cgdet.html", title="Change Details")


@app.route('/changedetails/changepassword', methods=['GET', 'POST'])
def changepassword():
    print(session['username'])
    user = session['username']
    if request.method == 'POST':
        oldpassword = request.form['lpass']
        newpassword = request.form['npass']
        confirm_new = request.form['cnpass']
        db = MySQLdb.connect(host="127.0.0.1", user="customer",
                             passwd="password", db="FlaskDB", port=5000)
        cursor = db.cursor()
        cursor.execute(
            '''SELECT password FROM MasterTable WHERE username = %s''', (user,))
        tup = cursor.fetchone()
        print(tup[0])
        if oldpassword == tup[0]:
            if newpassword == confirm_new:
                try:
                    cursor.execute(
                        '''UPDATE MasterTable SET password = %s WHERE username = %s''', (newpassword, user))
                    print("MasterTable updated")
                    cursor.execute(
                        '''UPDATE Users SET password = %s WHERE username = %s''', (newpassword, user))
                    print("Users updated")
                    cursor.execute(
                        '''UPDATE CustomerDetails SET password = %s WHERE username = %s''', (newpassword, user))
                    print("CustomerDetails updated")
                    db.commit()
                except:
                    print("Password Not Updated")
                    return render_template("cgdet.html", passworderror="Error in updating")

                finally:
                    print("Password Updated")
                    return render_template("cgdet.html", passwordsuccess="Password Updated")

    return redirect(url_for("details"))


@app.route('/changedetails/changeaddress', methods=['GET', 'POST'])
def changeaddress():
    user = session['username']
    if request.method == 'POST':
        newaddress = request.form['addr']
        db = MySQLdb.connect(host="127.0.0.1", user="customer",
                             passwd="password", db="FlaskDB", port=5000)
        cursor = db.cursor()
        try:

            cursor.execute(
                '''UPDATE MasterTable SET address = %s WHERE username = %s''', (newaddress, user))

        except:

            print(" Address not updated ")
            return render_template("cgdet.html", addresserror="Error in updating")

        finally:

            print(" Address Updated ")
            return render_template("cgdet.html", addresssuccess="Address Updated")
            db.commit()

    return redirect(url_for("details"))


@app.route('/signin')
def signin():
    if g.username:
        return redirect(url_for("userpage", user=session['username']))
    return render_template("signin.html", title="Sign In")


@app.route('/customers')
def section():
    if g.username:
        return redirect(url_for("userpage", user=session['username']))
    return render_template("signup.html", title="Login")


@app.route('/user/<user>')
def userpage(user):
    print(g.username)
    if g.username:
        db = MySQLdb.connect(host="127.0.0.1", user="customer",
                             passwd="password", db="FlaskDB", port=5000)
        cursor = db.cursor()
        cursor.execute(
            '''SELECT name, address, city, connection_id FROM MasterTable WHERE username = %s''', (user,))
        tup = cursor.fetchone()
        return render_template("myaccount.html", name=tup[0], address=tup[1], city=tup[2], conn_id=tup[3])
    return redirect(url_for("signin"))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin'))


@app.route('/signin/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        signinuser = request.form['uname'].strip()
        signinpass = request.form['pass']
        db = MySQLdb.connect(host="127.0.0.1", user="customer",
                             passwd="password", db="FlaskDB", port=5000)
        cursor = db.cursor()
        cursor.execute(
            '''SELECT username, password FROM Users where username = %s''', (signinuser,))
        result = cursor.fetchone()
        if ((signinuser == "") and (signinpass == "")):
            return render_template("signin.html", error="Please enter username and password")
        if not result:
            return render_template("signin.html", error="Invalid Username and Password")
        if (signinuser == result[0] and signinpass == result[1]):
            session['username'] = signinuser
            return redirect(url_for("userpage", user=signinuser))
    return render_template("signin.html", error="No such user. Please register")


@app.route('/filecomplaint')
def complaint():
    return render_template("complainpage.html")


@app.route('/filecomplaint/sendcomplain', methods=['GET', 'POST'])
def send_complain():
    if 'username' not in session:
        return render_template("signin.html")
    print("working")
    if request.method == 'POST':
        signinuser = session['username']
        complaint_id = signinuser[0:5]+str(datetime.now().hour)+str(
            datetime.now().minute)+str(datetime.now().second)
        complain = request.form['complainbox']
        print(complaint_id)
        try:
            db = MySQLdb.connect(
                host="127.0.0.1", user="customer", passwd="password", db="FlaskDB", port=5000)
            cursor = db.cursor()
            cursor.execute('''	INSERT INTO UserComplaints (username, complaint_id, complaint) values (%s,%s,%s)''',
                           (signinuser, complaint_id, complain,))
            db.commit()
            return render_template('complainpage.html', success="Complaint successfully submitted. Your complaint id is :"+complaint_id)
        except:
            return render_template('complainpage.html', error="Error submitting complaint")
    return render_template('complainpage.html', error="Some error occured")


@app.route('/forfeitconnection')
def forfeit():
    if session['username'] == None:
        return render_template("signin.html")
    return render_template("forfeit.html")


@app.route('/forfeitconnection/forfeit', methods=['GET', 'POST'])
def forfeitfinally():

    signinuser = session['username']
    if request.method == 'POST':
        if request.form['forfeit'] == 'Yes':
            currenttime = datetime.now().time

            try:
                db = MySQLdb.connect(
                    host="127.0.0.1", user="customer", passwd="password", db="FlaskDB", port=5000)
                cursor = db.cursor()
                cursor.execute(
                    '''DELETE FROM MasterTable where username = %s''', (signinuser,))
                cursor.execute(
                    '''DELETE FROM Users where username = %s''', (signinuser,))
                cursor.execute(
                    '''DELETE FROM CustomerDetails where username = %s''', (signinuser,))
                db.commit()
            except:
                return render_template("forfeit.html", error="Please try again.")
    return render_template("forfeit.html", success="Connection Forfeited", error="Eror")


@app.route('/payment')
def pay():
    return render_template("transactions.html",
                           months=['January', 'February', 'March'], amounts=['1000', '1420', '1233'],
                           paystatus=['Paid', 'Paid', 'Pending'])


@app.route('/requestservice')
def emergency():
    return render_template("emergencyservice.html")


#@app.errorhandler(404)
# def not_found(error):
  #flash("Sorry, the requested page is not found", "error")
  # return back.redirect()


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run("127.0.0.1", 5050, debug=True)
