from scheduling.ext.db import db
from marshmallow import fields, Schema

# from flask_sqlalchemy import orm


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

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update(scheduling, data):
        scheduling.title = data['title']
        scheduling.date = data['date']
        scheduling.start_time = data['start_time']
        scheduling.end_time = data['end_time']
        scheduling.room_number = data['room_number']
        scheduling.room_id = data['room_id']
        db.session.commit()

    @staticmethod
    def get_all_schedule():
        return Scheduling.query.all()

    @staticmethod
    def get_one_scheduling(schedule_id):
        return Scheduling.query.get(schedule_id)

    @staticmethod
    def filter_date(date):
        return Scheduling.query.filter(Scheduling.date == date).all()

    @staticmethod
    def filter_room(room):
        return Scheduling.query.filter(Scheduling.room_number == room).all()

    def __repr__(self):
        return f'schedule(id={self.id}, title={self.title}, date={self.date}, ' \
            f'start_time={self.start_time}, end_time{self.end_time}, ' \
            f'room_id={self.room_id}, room_number={self.room_number})!r'


class ScheduleSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(dump_only=True)
    date = fields.String(dump_only=True)
    start_time = fields.String(dump_only=True)
    end_time = fields.String(dump_only=True)
    room_id = fields.Integer(dump_only=True)
    room_number = fields.String(dump_only=True)
