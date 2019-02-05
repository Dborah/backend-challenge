from flask import Blueprint, jsonify
from flask_restful import Api, reqparse, Resource, fields

from scheduling.blueprints.api.models.room_model import Room
from scheduling.blueprints.api.models.scheduling_model import Scheduling

from scheduling.blueprints.api.utils import schedule_serializer

from scheduling.blueprints.api.errors import error_404


bp_rest = Blueprint('schedule_api', __name__, url_prefix='/api/v1')
api = Api(bp_rest)

schedule_parser = reqparse.RequestParser()
schedule_parser.add_argument('title', type=str)
schedule_parser.add_argument('date', type=str)
schedule_parser.add_argument('start_time', type=str)
schedule_parser.add_argument('end_time', type=str)
schedule_parser.add_argument('room_number', type=str)

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'date': fields.String,
    'start_time': fields.String,
    'end_time': fields.String,
    'room_id': fields.Integer,
    'room_number': fields.String
}


class Schedule(Resource):

    def __init__(self):
        self.args = schedule_parser.parse_args()

    def post(self):
        room_number = self.args['room_number']
        query_room = Room.filter_room(room_number)

        # Adicionar tratamento de erro para o número
        # Adicionar tratamento para reservar apenas se não houver
        # agendamento para o período de tempo

        schedule = Scheduling(
            title=self.args['title'],
            date=self.args['date'],
            start_time=self.args['start_time'],
            end_time=self.args['end_time'],
            room_id=query_room.id,
            room_number=query_room.room_number
        )
        schedule.save()
        resp = [{'message': 'New scheduling created successfully'}, {'id': schedule.id}]
        return resp, 201

    @staticmethod
    def get():
        query_schedules = Scheduling.get_all_schedule()
        resp = schedule_serializer(query_schedules)
        if len(resp) == 0:
            return [{'message': 'No registered scheduling.'}][0]
        resp = (resp, 200)
        return resp


class ScheduleItem(Resource):

    def __init__(self):
        self.args = schedule_parser.parse_args()

    @staticmethod
    def get(scheduling_id):
        query_scheduling = Scheduling.get_one_scheduling(scheduling_id)
        error_404(query_scheduling, scheduling_id, 'scheduling')

        room = Room.get_one_room(query_scheduling.room_id)

        resp = {
            'id': query_scheduling.id,
            'title': query_scheduling.title,
            'date': query_scheduling.date,
            'start_time': query_scheduling.start_time,
            'end_time': query_scheduling.end_time,
            'room_id': query_scheduling.room_id,
            'room_number': room.room_number
        }
        return jsonify(resp)

    def put(self, scheduling_id):
        query_scheduling = Scheduling.get_one_scheduling(scheduling_id)
        error_404(query_scheduling, scheduling_id, 'scheduling')

        room_number = self.args['room_number']
        query_room = Room.filter_room(room_number)
        # Adicionar erros de rooms

        data = {
            'title': self.args['title'],
            'date': self.args['date'],
            'start_time': self.args['start_time'],
            'end_time': self.args['end_time'],
            'room_number': room_number,
            'room_id': query_room.id
        }

        Scheduling.update(query_scheduling, data)
        resp = {'message': 'Scheduling updated successfully.'}
        return jsonify(resp)

    @staticmethod
    def delete(scheduling_id):
        query_scheduling = Scheduling.get_one_scheduling(scheduling_id)
        error_404(query_scheduling, scheduling_id, 'scheduling')
        query_scheduling.delete()
        # Adicionar resposta de retorno, tratar erros e conflitos
        # Resolver depois, deleta mais não retorna o json com a mensagem
        message = {'message': 'Scheduling deleted successfully.'}
        return message


def init_app(app):
    api.add_resource(Schedule, '/schedules')
    api.add_resource(ScheduleItem, '/schedules/<int:scheduling_id>')
    app.register_blueprint(bp_rest)
