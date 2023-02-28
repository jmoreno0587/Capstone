from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
db = SQLAlchemy()

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(255))
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    def __init__(self, userid, userName, firstName, lastName, email, password):
        self.userName = userName
        self.password = password
    def __repr__(self):
        return '<User %d>' % self.id