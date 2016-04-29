
import datetime
import os

from flask import Flask, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, json, send_from_directory, send_file
from sqlalchemy.orm.exc import NoResultFound

from config import WorkConfig
from model_hockey import User, User_action  # database types
from users.userRegistrator import UserSession

# config
app = Flask(__name__, static_folder=WorkConfig.STATIC_FOLDER)
#if ('TESTING' in globals()):
#    app.config.from_object(TestConfig)
#else:
app.config.from_object(WorkConfig)
db = SQLAlchemy(app)

# Additional import
#from flask.ext.httpauth import HTTPBasicAuth
#auth = HTTPBasicAuth()

# static routes
#print "App static folder: ", app.static_folder


@app.route('/')
def index():

    print "App static folder: ", app.static_folder
    user_session = UserSession(db.session, request)         # create user session
    resp = make_response("Hello from server", 200)
    user_session.setCookies(resp)
    return resp

hockey_base = "/Users/slash/Documents/Programming/_frontend_projects/hockey"


@app.route('/hockey/', methods=['GET'])
def hockey_index():
    print "get index"
    return send_file(hockey_base +"/index.html")

@app.route('/hockey/<path:path>')
def hockey_path(path):
    print hockey_base, path
    return send_from_directory(hockey_base, path)

'''
@app.route('/<path:path>', methods=['GET'])
def static_site(path):
    print "Static file request: ", path
    return app.send_static_file(path), 200
'''

''' ------------ API stuff begins
'''



@app.route('/api/registerevent', methods=['POST'])
def register_event():
    ''' Function parameter (JSON): event - type of the event
    :return: user's browser has cookies and session ID
    '''
    user_session = UserSession(db.session, request)         # create user session
    result = False
    try:                                # Try to get name from request
        #param = request.json
        jsonObject = request.json
        event = jsonObject['event']
    except:                             # set name to none if can't
        event = None
        print "Event is None, user session: %s"%(user_session.getUserID())
    else:
        if (event and event != User_action.REGISTER and event != User_action.CONNECT ):
            try:
                eventData=jsonObject['eventData']
            except KeyError as e:
                eventData = None
            user_session.registerEvent(db.session,event,request,data=eventData)
            print "registering event %s, with data %s"%(event, eventData)
            result = True
    resp = make_response(jsonify({'result' : result}), 200)
    user_session.setCookies(resp)
    return resp

## -------------- Server start
if __name__ == '__main__':
    #import logging
    #logging.basicConfig(filename='flask-error.log',level=logging.DEBUG)
    #print "App static folder: ", app.static_folder
    #print "Database: ", app.config['SQLALCHEMY_DATABASE_URI']
    app.run(host="192.168.2.253")

