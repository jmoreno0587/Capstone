from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
db = SQLAlchemy()

class Users(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(255))
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    email = db.Column(db.String(255))
    
    def __init__(self, userID, userName, firstName, lastName, email):
        self.userID = userID
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName
        self.email = email        
    def __repr__(self):
        return '<User %d>' % self.id

class Auths(db.Model):
    authID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(225))
    hashpassword = db.Column(db.String(225))
    def __init__(self, authID, username, hashpassword):
        self.authID = authID
        self.username = username
        self.hashpassword = hashpassword
    def __repr__(self):
        return '<Auths %s>' % self.username