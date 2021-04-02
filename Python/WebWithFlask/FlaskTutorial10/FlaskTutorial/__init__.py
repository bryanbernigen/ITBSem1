import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
from flask_bcrypt import Bcrypt
from flask_mail import Mail



app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
bcrypt = Bcrypt(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('dummy@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('dummydumdum')
mail = Mail(app)