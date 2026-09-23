import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI', 'sqlite:///db.sqlite3'
    )
    SECRET_KEY = os.environ.get('SECRET_KEY')