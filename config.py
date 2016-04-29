__author__ = 'DmitryGood'

# cloudsizer/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))
print basedir

#print "Basedir: ", basedir
#print "Static dir: ", static_folder


class BaseConfig(object):
    SECRET_KEY = 'this is my new secret key for hockey project'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
    SEND_FILE_MAX_AGE_DEFAULT = 30
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = basedir[:basedir.rfind('/')] + '/../../_frontend_projects/hockey'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


class WorkConfig(BaseConfig):
    DEBUG = True
    if os.environ.get('DATABASE_URL') is None:
        #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'hockey_v1.sqlite')
    else:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    LIVESERVER_PORT = 5000




