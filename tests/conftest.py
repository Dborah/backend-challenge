import pytest
import settings
# import sqlalchemy
from scheduling.app_factory import create_app
# from scheduling.ext.db import db

test_db = 'testdb'
env_name = 'testing'
DATABASE_URL = f'postgresql+psycopg2://postgres:root@localhost:5432/{test_db}'


@pytest.fixture(scope='session')
def app():
    app = create_app(settings.app_config[env_name])
    return app


@pytest.fixture
def client(app):
    client = app.test_client()
    context = app.test_request_context()
    context.push()
    return client
