import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\x87)\xfa+\xb3 7\xb8\xc17\xa1\x01\xb28\x9d\xb2\xee\x8f\xcb \x14_\x95E'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
