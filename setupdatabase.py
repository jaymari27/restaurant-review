import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from main import db, app, basedir

Migrate(app, db)

### This file will only run ONCE ###
from main import db, Customers, Reviews, Orders, Admin

# Create all tables
db.create_all()

# Add new entries in the table

lisa = Customers("Minci","Lisa")

# For multiple entries, use add_all([obj1, obj2])
db.session.add(lisa)
print("Before commit: ",lisa.customerid)

# Save all changes to database
db.session.commit()
print("After commit: ",lisa.customerid)
