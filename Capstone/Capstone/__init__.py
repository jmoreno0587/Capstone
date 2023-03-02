"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'some_random_key'


import Capstone.views
from Capstone.featAuth.auth import auth
app.register_blueprint(auth)

from Capstone.featUsers.user import usr
app.register_blueprint(usr)

from Capstone.featProjects.projects import proj
app.register_blueprint(proj)

from Capstone.models import db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Fang2023@database-capstone.czyt3syhmabj.us-east-1.rds.amazonaws.com:3306/testing'
db.init_app(app) #Add this line Before migrate line
db.create_all

