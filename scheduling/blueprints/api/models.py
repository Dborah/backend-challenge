from scheduling.ext.db import db
from marshmallow import fields, Schema


class Room(db.Model):
    """Room model."""
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String, nullable=False, unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update(room, data):
        room.room_number = data
        db.session.commit()
        return room

    @staticmethod
    def get_all_room():
        return Room.query.all()

    @staticmethod
    def get_one_room(room_id):
        return Room.query.get(room_id)

    def __repr__(self):
        return f'room(id={self.id}, room_number={self.room_number})'


class RoomSchema(Schema):
    id = fields.Int(dump_only=True)
    room_number = fields.String(dump_only=True)


class Schedule(db.Model):
    """Schedule model."""
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    first_period = db.Column(db.String(50), nullable=False)
    last_period = db.Column(db.String(50), nullable=False)

    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('schedule', lazy='dynamic'))

    def __repr__(self):
        return f'Schedule{self.title}'
