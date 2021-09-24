import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #db orm
db = SQLAlchemy(app) #database instance
bcrypt = Bcrypt(app)  #encryption instance
login_manager = LoginManager(app) #login manager instance
login_manager.login_view = 'login' #login manager view instance
login_manager.login_message_category = 'info' #login manager messenger instance
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'  #mail server 
app.config['MAIL_PORT'] = 587 #mail port
app.config['MAIL_USE_TLS'] = True #TLS hand shake
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER') #Mail username
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS') #mail userpassword
mail = Mail(app)   #mail app instance

from roadtraffic import routes
