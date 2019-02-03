import os
from scheduling.app_factory import create_app

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)
