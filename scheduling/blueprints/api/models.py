from scheduling.ext.db import db


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer)

    def __repr__(self):
        return f'Room(id={self.id}, room_number={self.room_number!r})'

    def __str__(self):
        return f'Room {self.room_number}'


class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    first_period = db.Column(db.String(50), nullable=False)
    last_period = db.Column(db.String(50), nullable=False)

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('schedule', lazy='dynamic'))

    def __repr__(self):
        return f'Schedule{self.title}'
