import os

# get folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'tasker.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'aflkepruo23098rlnfoi42sdfjkl29nbnepawepounv2343'

# define full path for database
DATABASE_PATH = os.path.join(basedir, DATABASE)
