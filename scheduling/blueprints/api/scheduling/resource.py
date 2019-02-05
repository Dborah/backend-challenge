from flask import Blueprint, jsonify
from flask_restful import Api, reqparse, Resource, fields

from scheduling.blueprints.api.models.scheduling_model import Scheduling

from scheduling.blueprints.api.utils import schedule_serializer

from scheduling.blueprints.api.errors import error_404


bp_rest = Blueprint('schedule_api', __name__, url_prefix='/api/v1')
api = Api(bp_rest)


schedule_parser = reqparse.RequestParser()
schedule_parser.add_argument('date', type=str)
schedule_parser.add_argument('room_number', type=str)


class SchedulesFilterDate(Resource):

    def __init__(self):
        self.args = schedule_parser.parse_args()

    def get(self):
        date = self.args['date']
        query_schedules = Scheduling.filter_date(date)
        response = schedule_serializer(query_schedules)
        return response


class SchedulesFilterRoom(Resource):

    def __init__(self):
        self.args = schedule_parser.parse_args()

    def get(self):
        room_number = self.args['room_number']
        query_schedules = Scheduling.filter_room(room_number)
        response = schedule_serializer(query_schedules)
        return response


def init_app(app):
    api.add_resource(SchedulesFilterDate, '/schedules/schedules', endpoint='schedules_filter')
    api.add_resource(SchedulesFilterRoom, '/schedules/rooms', endpoint='rooms_filter')
    app.register_blueprint(bp_rest)

