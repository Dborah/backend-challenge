from scheduling.ext.db import db
from marshmallow import fields, Schema

# from flask_sqlalchemy import orm


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

    @staticmethod
    def filter_room(room_number):
        # try:
        #     resp = Room.query.filter(Room.room_number == room_number).one()
        # except orm.exc.NoResultFound:
        #     raise room_number
        # return resp
        return Room.query.filter(Room.room_number == room_number).one()

    def __repr__(self):
        return f'rooms(id={self.id}, room_number={self.room_number})'


class RoomSchema(Schema):
    id = fields.Int(dump_only=True)
    room_number = fields.String(dump_only=True)


class Scheduling(db.Model):
    """Schedules model."""
    __tablename__ = 'scheduling'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.String(50), nullable=False)
    end_time = db.Column(db.String(50), nullable=False)

    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('scheduling', lazy='dynamic'))
    room_number = db.Column(db.String(50), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def update(scheduling, data):
        pass

    @staticmethod
    def get_all_schedule():
        return Scheduling.query.all()

    @staticmethod
    def get_one_scheduling(schedule_id):
        return Scheduling.query.get(schedule_id)

    def __repr__(self):
        return f'schedule(id={self.id}, title={self.title}, date={self.date}, ' \
            f'start_time={self.start_time}, end_time{self.end_time}, ' \
            f'room_id={self.room_id}, room_number={self.room_number}) '


class ScheduleSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(dump_only=True)
    date = fields.String(dump_only=True)
    start_time = fields.String(dump_only=True)
    end_time = fields.String(dump_only=True)
    room_id = fields.Integer(dump_only=True)
    room_number = fields.String(dump_only=True)
