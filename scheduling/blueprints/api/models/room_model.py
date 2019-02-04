from scheduling.ext.db import db
from marshmallow import fields, Schema

# from flask_sqlalchemy import orm


class RoomModel(db.Model):
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
        return RoomModel.query.all()

    @staticmethod
    def get_one_room(room_id):
        return RoomModel.query.get(room_id)

    @staticmethod
    def filter_room(room_number):
        # try:
        #     resp = Room.query.filter(Room.room_number == room_number).one()
        # except orm.exc.NoResultFound:
        #     raise room_number
        # return resp
        return RoomModel.query.filter(RoomModel.room_number == room_number).one()

    def __repr__(self):
        return f'room(id={self.id}, room_number={self.room_number})'


class RoomSchema(Schema):
    id = fields.Int(dump_only=True)
    room_number = fields.String(dump_only=True)
