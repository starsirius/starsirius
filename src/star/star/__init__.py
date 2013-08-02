from flask import Flask
from paste.deploy import appconfig
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.bcrypt import Bcrypt
import sys, os

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resources')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resources/static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
db = SQLAlchemy(app)
flask_bcrypt = Bcrypt(app)

def config_app(app=app, config_file="development.ini", relative_to="../"):
    print "\n"
    print "========================="
    print "Configuring application..."
    print "========================="
    raw_config = appconfig("config:"+config_file, relative_to=relative_to)
    for k in raw_config:
        app.config[k] = raw_config[k]
    return app

def connect_controllers():
    print "\n"
    print "========================="
    print "Connecting controllers..."
    print "========================="
    from star.controllers import *

def connect_db():
    print
    print "========================="
    print "Connecting database...   "
    print "========================="
    from star.models.core import *
    db.create_all()
