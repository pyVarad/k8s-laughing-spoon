import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-easy-to-guess'
    REDIS_HOST = "redis"
    REDIS_PORT = 6379 