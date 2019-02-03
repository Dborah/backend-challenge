from flask import Blueprint

bp = Blueprint('schedule_api', __name__)


@bp.route('/schedule')
def room():
    return 'Schedule'


def init_app(app):
    app.register_blueprint(bp)
