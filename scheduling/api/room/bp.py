from flask import Blueprint

bp = Blueprint('room_api', __name__)


@bp.route('/room')
def room():
    return 'Rooms'


def init_app(app):
    app.register_blueprint(bp)
