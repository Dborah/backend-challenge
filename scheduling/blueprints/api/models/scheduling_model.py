from scheduling.ext.db import db


class Scheduling(db.Model):
    """Schedules model."""
    __tablename__ = 'schedules'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    room_number = db.Column(db.Integer, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)

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
        scheduling.room_number = data['room_number']
        scheduling.room_id = data['room_id']
        db.session.commit()

    @staticmethod
    def get_schedules():
        return Scheduling.query.all()

    @staticmethod
    def get_scheduling(scheduling_id):
        return Scheduling.query.get(scheduling_id)

    @staticmethod
    def filter_date(date):
        return Scheduling.query.filter(Scheduling.date == date).all()

    @staticmethod
    def filter_room_number(room):
        return Scheduling.query.filter(Scheduling.room_number == room).all()

    @staticmethod
    def filter_schedules(date, room):
        return Scheduling.query.filter(
            db.and_(Scheduling.date == date, Scheduling.room_number == room)).all()

    def __repr__(self):
        return f'schedule(id={self.id}, title={self.title}, date={self.date}, room_number={self.room_number})'
