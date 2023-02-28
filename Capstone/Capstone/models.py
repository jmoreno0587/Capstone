from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return '<User %d>' % self.id