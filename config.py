import os

basedir = os.path.abspath(os.path.dirname(__file__)) # tell python to look at all files the same on any operating system


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACH_MODIFICATIONS =False
    
