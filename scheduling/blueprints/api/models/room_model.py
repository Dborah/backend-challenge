from scheduling.ext.db import db

from flask_sqlalchemy import orm


class Room(db.Model):
    """Room model."""
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer, nullable=False, unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update(room, room_number):
        room.room_number = room_number
        db.session.commit()
        return room

    @staticmethod
    def get_rooms():
        return Room.query.all()

    @staticmethod
    def get_room(room_id):
        return Room.query.get(room_id)

    @staticmethod
    def filter_room(room_number):
        try:
            room = Room.query.filter(Room.room_number == room_number).one()
        except orm.exc.NoResultFound:
            return None
        return room

    def __repr__(self):
        return f'rooms(id={self.id}, room_number={self.room_number})'
