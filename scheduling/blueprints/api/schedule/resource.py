from flask import Blueprint, jsonify
from flask_restful import Api, reqparse, Resource

bp_rest = Blueprint('schedule_api', __name__, url_prefix='/api/v1')
api = Api(bp_rest)

schedule_parser = reqparse.RequestParser()
schedule_parser.add_argument('title', type=str)
schedule_parser.add_argument('first_period', type=str)
schedule_parser.add_argument('last_period', type=str)


class ScheduleAPI(Resource):

    def post(self):
        args = schedule_parser.args()
        schedule = {
            'title': args['title'],
            'first_period': args['first_period'],
            'last_period': args['last_period']
        }
        return jsonify(schedule)


def init_app(app):
    api.add_resource(ScheduleAPI, 'schedule')
    app.register_blueprint(bp_rest)
