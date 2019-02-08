import os


class Config:
    DEBUG = os.getenv('DEBUG') or False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')


class Development(Config):
    """Development environment configuration"""
    DEBUG = True


class Production(Config):
    """Production environment configurations"""
    DEBUG = False
    TESTING = False


class Testing(Config):
    """Testing environment configurations"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
