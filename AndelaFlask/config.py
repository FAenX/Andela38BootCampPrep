import os

# You need to replace the next values with the appropriate values for
# your configuration

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DATABASE_URI = ''


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True