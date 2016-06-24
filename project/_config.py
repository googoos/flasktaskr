"""flasktaskr configuration."""

import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True
SECRET_KEY = 'YourSecretKey'

# define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

DEBUG = False
