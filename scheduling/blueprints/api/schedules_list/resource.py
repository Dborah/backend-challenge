from flask import Blueprint
from flask_restful import Api, reqparse, Resource

from scheduling.blueprints.api.models.scheduling_model import Scheduling as SchedulingModel

from scheduling.blueprints.api.utils import schedule_serializer


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

        query_schedules = SchedulingModel.filter_schedules(date, room_number)
        response = schedule_serializer(query_schedules)
        return response


def init_app(app):
    api.add_resource(SchedulesFilter, '/schedules', endpoint='schedules_filter')
    app.register_blueprint(bp_rest)

