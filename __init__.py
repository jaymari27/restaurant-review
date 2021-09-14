import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager

# For Admin Login
login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

### For database
# __file__      = absolute path where the database will created
basedir = os.path.abspath(os.path.abspath(__file__))
# postgresql    = database
# postgres      = username
# 023577        = password
# postgres      = database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:023577@localhost/postgres'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///'+os.path.join(basedir,'data.postgres')

# Tracks changes in SQL. We don't need it here, so set it to False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# For queries
db = SQLAlchemy(app)

Migrate(app, db)

# Initialize so it will handle your logins
login_manager.init_app(app)
# The view in which the login will occur
login_manager.login_view = 'login'