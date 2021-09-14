from flask.helpers import url_for
from werkzeug.utils import redirect
from __init__ import app
from models import Admin
from flask import render_template, request
from flask_login import login_required

# Admin Home
@app.route('/home')
@login_required
def adminHome():
    return render_template('home.html') 

# Admin Login
@app.route('/login')
def loginPage():
    return render_template('login.html')

# Admin Login Attempt
@app.route('/login/admin', methods=['POST'])
def adminlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        adminList = Admin.query.all()

        # Message for invalid credentials
        message = "Username and/or password does not match our records."
        #print(adminList)

        if (username == adminList.username and password == adminList.password):
            return redirect(url_for('adminHome'))
        else:
            return render_template('login.html', message=message)