from flask import Flask
from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO, emit
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['MONGO_DBNAME']='SHN'
app.config['MONGO_URI']=os.getenv('URI')


#setup_mongodb
mongdb_client=PyMongo(app)
db=mongdb_client.db

#db = SQLAlchemy(app)
#bcrypt=Bcrypt(app)


#login_manager = LoginManager(app)
#login_manager.login_view = "login_page"
#login_manager.login_message_category = "info"


from application import routes
