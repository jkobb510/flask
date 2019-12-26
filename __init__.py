import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


loginmanager = LoginManager()

app = Flask(__name__)

app.config['SECRETKEY'] = 'mysecretkey'
basedir = os.path.abspath(os.pardir.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy()
Migrate(app,db)

loginmanager.init_app(app)
loginmanager.login_view = 'login'
