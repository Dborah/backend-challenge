from flask import Flask

from scheduling.ext.db import db


def create_app():
    app = Flask(__name__)

    # Initialize Extensions
    register_blueprint(app)

    # Initialize blueprints
    register_blueprint(app)

    return app


def register_blueprint(app):
    """Register Blueprints"""
    from scheduling.api.room import bp as room_api
    from scheduling.api.schedule import bp as schedule_api

    room_api.init_app(app)
    schedule_api.init_app(app)
    return app


def register_extensions(app):
    """Register extensions."""
    db.init_app(app)
    return app
