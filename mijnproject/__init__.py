import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'skaioenvipqwhe'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from mijnproject.docenten.views import docenten_blueprint
from mijnproject.studenten.views import studenten_blueprint

app.register_blueprint(studenten_blueprint,url_prefix="/studenten")
app.register_blueprint(docenten_blueprint,url_prefix='/docenten')