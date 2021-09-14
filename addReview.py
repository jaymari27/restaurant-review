from __init__ import db, app
from models import Customers, Reviews, Orders
from flask import render_template, request

# On Submit
@app.route('/submit', methods=['POST'])
def submit():
    # Making sure that the method is POST
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        orderno = request.form['orderno']
        waiter = request.form['waiter']
        rating = request.form['rating']
        comments = request.form['comments']

        # Data validation
        customerEmpty = False
        waiterEmpty = False
        commentsEmpty = False
        ordernoEmpty = False
        
        if (firstname == "" or lastname == ""):
            customerEmpty = True
        if (waiter == ""):
            waiterEmpty = True
        if (comments == ""):
            commentsEmpty = True
            comments = "The customer did not enter any comment."
        if (orderno == ""):
            ordernoEmpty = True
        if (customerEmpty == True or waiterEmpty == True or ordernoEmpty == True):
            return render_template('form.html', customerEmpty=customerEmpty,waiterEmpty=waiterEmpty, ordernoEmpty=ordernoEmpty)
        else:
            return render_template('success.html', firstname=firstname, lastname=lastname, waiter=waiter, comments=comments, rating=rating, orderno=orderno)