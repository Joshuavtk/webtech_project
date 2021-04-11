from filmsite import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64))
    user_email = db.Column(db.String(320), unique=True)
    user_password = db.Column(db.String(128))
    creation_date = db.Column(db.DateTime)

    def check_password(self, password):
        return check_password_hash(self.user_password, password)



class Movie(UserMixin, db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    director_id = db.Column(db.Integer,db.ForeignKey('directors.id'))
    release_year = db.Column(db.Integer)
    roles = db.relationship('Role',backref='movies')
    """Nog toe te voegen
    Film
    Bezoekers gegevens
    Opbrengst
    Regiseur
    Producent
    Hoofdrolspelers
    Speelduur
    Jaar van uitkomst
    Genre
    """

class Actor(UserMixin, db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(64))
    roles = db.relationship('Role',backref='actors')

class Director(UserMixin, db.Model):
    def __repr__(self):
        return self.first_name + ' ' + self.last_name
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='directors')

class Role(UserMixin, db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer,db.ForeignKey('movies.id'))
    actor_id = db.Column(db.Integer,db.ForeignKey('actors.id'))
    playing_as = db.Column(db.String(64))
