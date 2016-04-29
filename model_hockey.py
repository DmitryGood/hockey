__author__ = 'DmitryGood'
from sqlalchemy import Column, String, Integer, ForeignKey, PickleType, Float, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import pickle
import datetime
import hashlib


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ''' the table to store user

    '''
    USER_ROLE_ADMIN = 'admin'
    USER_ROLE_USER = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cookie = Column(String(100), nullable=False)
    name = Column(String(100))
    created = Column(DateTime, nullable=False)
    userdata = Column(PickleType)
    role = Column(String(20), nullable=False, default=USER_ROLE_USER)

    def __init__(self, name=None, role=USER_ROLE_USER, userdata=None):
        self.name = name
        self.role = role
        self.userdata = userdata
        self.created = datetime.datetime.now()
        # create cookie for user as hash of his first entrance time
        self.cookie = hashlib.sha1(str(self.created)).hexdigest() # create cookie for user as hash of his first entrance time
        return

    def getCookie(self):
        return self.cookie

class User_action(Base):
    __tablename__ = 'user_action'
    ''' Table for tracking user activity
        user - user data
        time - time of the event
        action - user action from the list
        ip - IP of connection
        repeated - False if the first connection, True, if repeated (user had cookie already)
        data - additional data (uploaded file name, etc.)
    '''
    REGISTER = 100;
    CONNECT = 200;
    START_GAME = 300;
    END_GAME = 400;


    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', uselist = False)
    time = Column(DateTime, nullable=False)
    action = Column(Integer)
    ip = Column(String(20))
    repeated = Column(Boolean)
    data = Column(PickleType)

    def __init__(self, user_id, action=None, ip=None, repeated=False):
        self.user_id = user_id
        self. time = datetime.datetime.now()
        self.action = action
        self.ip = ip
        self.repeated = repeated

