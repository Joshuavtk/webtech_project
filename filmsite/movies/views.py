from flask import Blueprint, render_template, redirect, url_for
from filmsite import db, flash, login_required
from filmsite.movies.forms import CreateForm, DelForm
from filmsite.models import Movie, Director

movies_blueprint = Blueprint('movies',
                               __name__,
                               template_folder='templates')


def render(name, form):
    url = 'movies/'
    return render_template(url + name + '.html', form=form)


@movies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = CreateForm()

    directors = Director.query.all()
    directors_list=[(i.id, i.first_name + ' ' + i.last_name) for i in directors]
    form.director_id.choices = directors_list

    if form.validate_on_submit():
    
        new_movie = Movie(
            title=form.title.data, 
            release_year=form.release_year.data, 
            director_id = form.director_id.data)

        db.session.add(new_movie)
        db.session.commit()

        flash("Nieuwe film succesvol toegevoegd.")
        return redirect(url_for("index"))
    return render('create', form)


@movies_blueprint.route('/list')
def list():
    movies = Movie.query.all()
    return render_template('movies/all.html', movies=movies)


@movies_blueprint.route('/<movie_id>/delete', methods=['GET', 'POST'])
def delete(movie_id):

    movie = Movie.query.filter_by(id=movie_id).first()
    form = DelForm(obj=movie)

    if form.validate_on_submit():
        db.session.delete(movie)
        db.session.commit()

        flash("Film succesvol verwijderd.")

        return redirect(url_for('movies.list'))
    return render('delete', form)



@movies_blueprint.route("/<movie_id>", methods=['GET', 'POST'])
def show(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()

    return render_template("movies/view.html", movie=movie)


@movies_blueprint.route("/<movie_id>/edit", methods=['GET', 'POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    form = CreateForm(obj=movie)

    directors = Director.query.all()
    directors_list=[(i.id, i.first_name + ' ' + i.last_name) for i in directors]
    form.director_id.choices = directors_list

    if form.validate_on_submit():

        movie.title = form.title.data
        movie.release_year = form.release_year.data
        movie.director_id = form.director_id.data

        db.session.add(movie)
        db.session.commit()

        flash("Film succesvol bijgewerkt.")
        return redirect(url_for('movies.show', movie_id = movie.id))

    return render_template("movies/edit.html", form=form, movie=movie)