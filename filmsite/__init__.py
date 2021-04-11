import os
from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, Email

app = Flask(__name__)

app.config['SECRET_KEY'] = 'skaioenvipqwhe'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)

from filmsite.movies.views import movies_blueprint
from filmsite.actors.views import actors_blueprint
from filmsite.users.views import users_blueprint
from filmsite.directors.views import directors_blueprint

app.register_blueprint(movies_blueprint,url_prefix='/movies')
app.register_blueprint(actors_blueprint,url_prefix="/actors")
app.register_blueprint(users_blueprint,url_prefix="/users")
app.register_blueprint(directors_blueprint,url_prefix="/directors")