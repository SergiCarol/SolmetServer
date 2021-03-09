from flask_sqlalchemy import SQLAlchemy
from mongoengine import *


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    api_key = db.Column(db.String(1000), unique=True)

    def __repr__(self):
        return '<email {}>'.format(self.email)

class Arduino(db.Model):
    __tablename__ = 'arduino'

    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(1000), unique=True)
    arduino_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='user', lazy=True)

class Schedule(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100))
    start_time = db.Column(db.String(100))
    end_time = db.Column(db.String(100))
    active = db.Column(db.Integer)
    arduino_id = db.Column(db.String(100), db.ForeignKey('arduino.api_key'))
    arduino = db.relationship('Arduino', backref='arduino', lazy=True)


class Data(Document):
    temperature = FloatField(required=True)
    humidity = FloatField(max_length=50)
    water_temperature = FloatField(max_length=50)
    water_ph = FloatField(max_length=50)
    water_electrodes = FloatField(max_length=50)
    api_key = StringField(max_length=50)

from app import app
db = SQLAlchemy(app)
