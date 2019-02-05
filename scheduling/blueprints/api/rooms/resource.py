from flask import Blueprint
from flask_restful import Api, reqparse, Resource, fields

from scheduling.blueprints.api.models.room_model import Room as RoomModel
from scheduling.blueprints.api.models.scheduling_model import Scheduling as SchedulingModel

from scheduling.blueprints.api.responses import (
    resp_does_not_exist,
    resp_already_exists,
    resp_created_successfully,
    resp_update_successfully,
    resp_delete_successfully,
    resp_room_linked_to_schedule
    )

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

    def post(self):
        room_number = self.args['room_number']
        query_room = RoomModel.filter_room(room_number)

        if not query_room:
            room = RoomModel(room_number=room_number)
            room.save()
            return resp_created_successfully('room')

        if query_room.room_number == room_number:
            return resp_already_exists('Room')


class RoomItem(Resource):

    def __init__(self):
        self.args = room_parser.parse_args()

    def put(self, room_id):
        room_number = self.args['room_number']
        filter_room = RoomModel.filter_room(room_number)

        if not filter_room:
            query_room = RoomModel.get_room(room_id)
            resp_does_not_exist(query_room, f'Room {room_id}')
            RoomModel.update(query_room, room_number)
            return resp_update_successfully('Room')

        if filter_room.room_number == room_number:
            return resp_already_exists('Room')

    @staticmethod
    def delete(room_id):
        query_room = RoomModel.get_room(room_id)
        resp_does_not_exist(query_room, f'Room {room_id}')

        room_filter = SchedulingModel.filter_room_id(room_id)
        if room_filter:
            return resp_room_linked_to_schedule(f'{room_id}')
        query_room.delete()
        return resp_delete_successfully('Room')


def init_app(app):
    api.add_resource(Rooms, '/rooms', endpoint='rooms')
    api.add_resource(RoomItem, '/rooms/<int:room_id>', endpoint='room')
    app.register_blueprint(bp_rest)
