# -*- coding: utf-8 -*-
from os import getenv
from scheduling.app_factory import create_app

app = create_app(getenv('FLASK_ENV') or 'default')
