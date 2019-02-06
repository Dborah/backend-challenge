from flask import Blueprint
from flask_restful import Api, reqparse, Resource

from scheduling.blueprints.api.models.scheduling_model import Scheduling as SchedulingModel

from scheduling.blueprints.api.utils import schedule_serializer

from scheduling.blueprints.api.responses import (
    resp_does_not_exist,
    resp_successful
    )

bp_rest = Blueprint('schedule_api', __name__, url_prefix='/api/v1')
api = Api(bp_rest)


schedule_parser = reqparse.RequestParser()
schedule_parser.add_argument('date', type=str)
schedule_parser.add_argument('room', type=str)


class SchedulesFilter(Resource):

    def __init__(self):
        self.args = schedule_parser.parse_args()

    def get(self):
        date = self.args['date']
        room_number = self.args['room_number']

        if not date and not room_number:
            return None

        if not date:
            query_schedules = SchedulingModel.filter_room_number(room_number)
            serialized = schedule_serializer(query_schedules)
            return resp_successful(serialized)

        if not room_number:
            query_schedules = SchedulingModel.filter_date(date)
            serialized = schedule_serializer(query_schedules)
            return resp_successful(serialized)

        if not SchedulingModel.filter_date(date):
            return resp_does_not_exist(None, 'Date')

        if not SchedulingModel.filter_room_number(room_number):
            return resp_does_not_exist(None, 'Room')

        query_schedules = SchedulingModel.filter_schedules(date, room_number)
        serialized = schedule_serializer(query_schedules)
        return resp_successful(serialized)


def init_app(app):
    api.add_resource(SchedulesFilter, '/schedules', endpoint='schedules_filter')
    app.register_blueprint(bp_rest)

