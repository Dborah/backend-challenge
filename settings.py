# from decouple import config
#
# DEBUG = config('DEBUG', default=False, cast=bool)
# DATABASE_LOCATION = config('DATABASE_LOCATION')
# DATABASE_NAME = config('DATABASE_NAME')
# SQLALCHEMY_DATABASE_URI = f'{DATABASE_LOCATION}/{DATABASE_NAME}'
# SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)
# DEBUG_TB_INTERCEPT_REDIRECTS = False
# SECRET_KEY = config('SECRET_KEY')
import os


class Development(object):
    """Development environment configuration"""
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Production(object):
    """Production environment configurations"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')


class Testing(object):
    pass


app_config = {
    'development': Development,
    'production': Production,
}
