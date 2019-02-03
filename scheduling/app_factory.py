from flask import Flask

from scheduling.ext.db import db
from scheduling.ext import migrate

from settings import app_config


def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    # Initialize Extensions
    register_extensions(app)

    # Initialize Blueprints
    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register Blueprints"""
    from scheduling.blueprints.api.room import resource as room_api
    from scheduling.blueprints.api.schedule import bp as schedule_api

    room_api.init_app(app)
    schedule_api.init_app(app)
    return app


def register_extensions(app):
    """Register extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    return app
