from settings import app_config
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # Initialize Extensions
    register_extensions(app)

    # Initialize Blueprints
    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register Blueprints"""
    from scheduling.blueprints.api.rooms import resource as room_api
    from scheduling.blueprints.api.schedules import resource as schedules_api
    from scheduling.blueprints.api.schedules_list import resource as schedules_list_filter_api

    room_api.init_app(app)
    schedules_api.init_app(app)
    schedules_list_filter_api.init_app(app)
    return app


def register_extensions(app):
    """Register extensions."""
    from scheduling.ext.db import db
    from scheduling.ext import migrate

    db.init_app(app)
    migrate.init_app(app, db)
    return app
