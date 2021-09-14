from __init__ import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_manager

### Models
# Creating a model, which is used to create database

# Customer List
class Customers(db.Model):
    # Defining the table and its fields
    __tablename__ = 'tbl_customerlist'
    customerid = db.Column(db.Integer,primary_key=True)
    lastname = db.Column(db.String(255))
    firstname = db.Column(db.String(255))

    # Initializer
    def __init__(self, lastname, firstname):
        self.lastname = lastname;
        self.firstname = firstname;
    
    def __repr__(self):
        return f"Customer Info:\nLast name: {self.lastname}\nFirst name: {self.firstname}"

# Review List
class Reviews(db.Model):
    __tablename__ = "tbl_reviewlist"
    reviewid = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.Integer)
    orderid = db.Column(db.String(6))
    ratingid = db.Column(db.Integer)
    review = db.Column(db.String(255))

     # Initializer
    def __init__(self, customerid, ratingid, review, orderid):
        self.customerid = customerid
        self.ratingid = ratingid
        self.review = review
        self.orderid = orderid
    
    def __repr__(self):
        return f"ReviewID: {self.customerid}\nRatingID: {self.ratingid}\nOrderID:{self.orderid}\nReview: {self.review}\n"

# Order List
class Orders(db.Model):
    __tablename__ = "tbl_orderlist"
    orderid = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.Integer)
    orderno = db.Column(db.String(6))
    discountcode = db.Column(db.String(8))

     # Initializer
    def __init__(self, customerid, orderno, discountcode):
        self.customerid = customerid
        self.orderno = orderno
        self.discountcode = discountcode

    def __repr__(self):
        return f"Order Info:\nOrder ID: {self.orderid}\nDiscount Code: {self.discountcode}"

################
# Admin

# Pages accessible when logged in
@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)

class Admin(db.Model, UserMixin):
    __tablename__ = "tbl_admin"
    adminid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    password_hash = db.Column(db.String(128))

    def __init__(self, username, password_hash):
        self.username = username
        # Saving actual string, not hash
        self.password = generate_password_hash(password_hash)

    def __repr__(self):
        return f"Admin Credentials:\nUsername: {self.username}\nPassword: {self.password}"
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)