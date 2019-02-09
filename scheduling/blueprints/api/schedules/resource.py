from flask import Blueprint
from flask_restful import Api, reqparse, Resource, fields

from scheduling.blueprints.api.models.room_model import Room as RoomModel
from scheduling.blueprints.api.models.scheduling_model import Scheduling as SchedulingModel

from scheduling.blueprints.api.responses import (
    resp_created_successfully,
    resp_update_successfully,
    resp_delete_successfully
    )

from scheduling.blueprints.api.errors import (
    error_does_not_exist,
    error_unavailable,
    )

bp_rest = Blueprint('schedules_api', __name__, url_prefix='/api/v1')
api = Api(bp_rest)

schedule_parser = reqparse.RequestParser()
schedule_parser.add_argument('title', type=str)
schedule_parser.add_argument('date', type=str)
schedule_parser.add_argument('room_number', type=int)

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'date': fields.String,
    'room_number': fields.Integer,
    'room_id': fields.Integer
}


class Schedule(Resource):

    def __init__(self):
        self.args = schedule_parser.parse_args()

    def post(self):
        title = self.args['title']
        date = self.args['date']
        room_number = self.args['room_number']

        query_room = RoomModel.filter_room(room_number)
        if not query_room:
            return error_does_not_exist(query_room, 'Room')

        if SchedulingModel.filter_schedules(date, room_number):
            return error_unavailable()

        schedule = SchedulingModel(
            title=title,
            date=date,
            room_number=room_number,
            room_id=query_room.id
        )
        schedule.save()
        return resp_created_successfully('scheduling')


class ScheduleItem(Resource):

    def __init__(self):
        self.args = schedule_parser.parse_args()

    def put(self, scheduling_id):
        title = self.args['title']
        date = self.args['date']
        room_number = self.args['room_number']

        query_scheduling = SchedulingModel.get_scheduling(scheduling_id)
        if not query_scheduling:
            return error_does_not_exist(None, f'Scheduling {scheduling_id}')

        filter_room = RoomModel.filter_room(room_number)
        if not filter_room:
            error_does_not_exist(filter_room, f'Room {room_number}')

        if SchedulingModel.filter_schedules(date, room_number):
            return error_unavailable()

        data = {
            'title': title,
            'date': date,
            'room_number': room_number,
            'room_id': filter_room.id
        }
        SchedulingModel.update(query_scheduling, data)
        return resp_update_successfully('Scheduling')

    @staticmethod
    def delete(scheduling_id):
        query_scheduling = SchedulingModel.get_scheduling(scheduling_id)
        error_does_not_exist(query_scheduling, f'Scheduling {scheduling_id}')
        query_scheduling.delete()
        return resp_delete_successfully('Scheduling')


def init_app(app):
    api.add_resource(Schedule, '/schedules', endpoint='schedules')
    api.add_resource(ScheduleItem, '/schedules/<int:scheduling_id>', endpoint='schedule')
    app.register_blueprint(bp_rest)
