from flask import Blueprint, jsonify
# from flask import current_app as app
from flask_restful import Api, reqparse, Resource


bp_rest = Blueprint('room_api', __name__, url_prefix='/api/v1')
api = Api(bp_rest)

# room_parse = reqparse.RequestParser()
# room_parse.add_argument('room_number')


class RoomAPI(Resource):
    def post(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


room_list_parser = reqparse.RequestParser()
room_list_parser.add_argument('room_number')


class RoomListAPI(Resource):
    def get(self):
        return jsonify({'Room': 'Resource!'})


def init_app(app):
    api.add_resource(RoomListAPI, '/rooms', endpoint='room')
    api.add_resource(RoomAPI, '/api/v1/rooms/<room_id>', endpoint='rooms')
    app.register_blueprint(bp_rest)
