from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

from datetime import datetime

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String(10))
    status = db.Column(db.String(20), default="available")
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    lock_time = db.Column(db.DateTime, nullable=True)  # 👈 ADD THIS