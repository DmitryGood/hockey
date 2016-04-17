from migrate.versioning import api
from config import WorkConfig
#from config import SQLALCHEMY_DATABASE_URI
#from config import SQLALCHEMY_MIGRATE_REPO
print "Database: ", WorkConfig.SQLALCHEMY_DATABASE_URI
print "Migrate REPO: ", WorkConfig.SQLALCHEMY_MIGRATE_REPO


api.upgrade(WorkConfig.SQLALCHEMY_DATABASE_URI, WorkConfig.SQLALCHEMY_MIGRATE_REPO)
print 'Current database version: ' + str(api.db_version(WorkConfig.SQLALCHEMY_DATABASE_URI, WorkConfig.SQLALCHEMY_MIGRATE_REPO))
