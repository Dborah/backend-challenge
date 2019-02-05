from flask import Blueprint, jsonify
from flask_restful import Api, reqparse, Resource, fields

from scheduling.blueprints.api.models.room_model import Room

from scheduling.blueprints.api.utils import room_serializer

from scheduling.blueprints.api.errors import error_404

bp_rest = Blueprint('room_api', __name__, url_prefix='/api/v1')
api = Api(bp_rest)

room_parser = reqparse.RequestParser()
room_parser.add_argument('room_number', type=str)

resource_fields = {
    'id': fields.Integer,
    'room_number': fields.String
}


class Rooms(Resource):

    def __init__(self):
        self.args = room_parser.parse_args()

    # @staticmethod
    # def get():
    #     query = Room.get_all_room()
    #     resp = room_serializer(query)
    #     if len(resp) == 0:
    #         return [{'message': 'No registered rooms.'}][0]
    #     resp = (resp, 200)
    #     return resp

    def post(self):
        room_id = self.args['room_number']
        room = Room(room_number=room_id)
        room.save()
        # Adicionar erro de conflito com sala já existente
        resp = [{'message': 'New rooms created successfully.'}, {'rooms': room_id}]
        return resp, 201


class RoomItem(Resource):

    def __init__(self):
        self.args = room_parser.parse_args()

    # @staticmethod
    # def get(room_id):
    #     query_room = Room.get_one_room(room_id)
    #     error_404(query_room, room_id, 'rooms')
    #     resp = {'id': query_room.id, 'room_number': query_room.room_number}
    #     return jsonify(resp)

    def put(self, room_id):
        room_number = self.args['room_number']
        query_room = Room.get_one_room(room_id)
        error_404(query_room, room_id, 'rooms')
        # Adicionar erro de conflito com sala já existente
        room = Room.update(query_room, room_number)
        resp = {'message': 'Room updated successfully.'}, {'room_number': room.room_number}
        return jsonify(resp)

    @staticmethod
    def delete(room_id):
        query_room = Room.get_one_room(room_id)
        error_404(query_room, room_id, 'rooms')
        query_room.delete()
        # Adicionar resposta de retorno, tratar erros e conflitos
        return query_room


def init_app(app):
    api.add_resource(Rooms, '/rooms', endpoint='rooms')
    api.add_resource(RoomItem, '/rooms/<int:room_id>', endpoint='room')
    app.register_blueprint(bp_rest)
