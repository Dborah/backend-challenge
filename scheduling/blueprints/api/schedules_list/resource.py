from flask import Blueprint
from flask_restful import Api, reqparse, Resource

from scheduling.blueprints.api.models.scheduling_model import Scheduling as SchedulingModel
from scheduling.blueprints.api.models.room_model import Room as RoomModel

from scheduling.blueprints.api.utils import schedule_serializer

from scheduling.blueprints.api.responses import (
    resp_does_not_exist,
    resp_successful,
    resp_not_meeting
    )

bp_rest = Blueprint('schedule_api', __name__, url_prefix='/api/v1')
api = Api(bp_rest)


schedule_parser = reqparse.RequestParser()
schedule_parser.add_argument('date', type=str)
schedule_parser.add_argument('room_number', type=str)


class SchedulesFilter(Resource):

    def __init__(self):
        self.args = schedule_parser.parse_args()

    def get(self):
        date = self.args['date']
        room_number = self.args['room_number']

        if not date and not room_number:
            query_schedules = SchedulingModel.get_schedules()
            if not query_schedules:
                return resp_does_not_exist(None, 'Data')
            serialized = schedule_serializer(query_schedules)
            return resp_successful(serialized)

        if not date:
            query_filter_room_number = SchedulingModel.filter_room_number(room_number)
            if not query_filter_room_number:
                validate_room(room_number)
                return resp_not_meeting('room')
            serialized = schedule_serializer(query_filter_room_number)
            return resp_successful(serialized)

        if not room_number:
            query_filter_date = SchedulingModel.filter_date(date)
            if not query_filter_date:
                return resp_not_meeting('date')
            serialized = schedule_serializer(query_filter_date)
            return resp_successful(serialized)

        validate_room(room_number)

        query_schedules = SchedulingModel.filter_schedules(date, room_number)
        if not query_schedules:
            validate_room(room_number)
            return resp_not_meeting('meeting')

        serialized = schedule_serializer(query_schedules)
        return resp_successful(serialized)


def validate_room(room_number):
    """
    Checks if room exists.

    :param room_number: int number.
    :return: json response {'message': 'Room does not exist.'}
    """
    query_filter_room = RoomModel.filter_room(room_number)
    if not query_filter_room:
        return resp_does_not_exist(None, 'Room')


def init_app(app):
    api.add_resource(SchedulesFilter, '/schedules', endpoint='schedules_filter')
    app.register_blueprint(bp_rest)

