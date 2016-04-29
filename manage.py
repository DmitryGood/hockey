__author__ = 'DmitryGood'

# manage.py

from flask_script import Manager
#from flask.ext.migrate import Migrate, MigrateCommand
#from project import app, db
from model_hockey import Base, User, User_action
from config import WorkConfig
from flask_APIdefinition import app, db
#from . import app, db


#migrate = Migrate(app, db)

# migrations
#manager.add_command('db', MigrateCommand)
#db = SQLAlchemy(app)
#db.init_app(app)

#app = Flask(__name__,  static_folder=WorkConfig.STATIC_FOLDER)
app.config.from_object(WorkConfig)

#db=SQLAlchemy(app)
#engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
#session = sessionmaker(bind= db.engine)()

manager = Manager(app)

#Base.metadata.bind = engine
#db.session = sessionmaker(bind=engine)()
#engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

#Base.metadata.bind = engine
#print "Start: App static folder: ", app.static_folder

# ----------- Private methods

# -----------

@manager.command
def create_db():
    """Creates the db tables ."""
    Base.metadata.create_all(db.engine)
    print "--- Create database"



@manager.command
def drop_db():
    """Drops the db tables."""
    Base.metadata.drop_all(db.engine)
    print "--- Drop database"

@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(name='admin@test.com', role=User.USER_ROLE_ADMIN))
    db.session.commit()
    print "--- Create user 'admin@test.com'"

@manager.command
def create_data():
    print "----- Re-create database data"
    drop_db()
    create_db()
    create_admin()

@manager.command
def run_public():
    app.run(host="0.0.0.0", debug=True)

@manager.command
def run_hand():
    print "App static folder: ", app.static_folder
    app.run()

@manager.command
def run_ssl():
    app.run(host="0.0.0.0", debug=True, ssl_context=app.config['SSL_CONTEXT'])

if __name__ == '__main__':
    print "App static folder: ", app.static_folder
    print "Database: ", app.config['SQLALCHEMY_DATABASE_URI']
    manager.run()

