from . import Config


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True