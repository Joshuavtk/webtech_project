from flask import Blueprint, render_template, redirect, url_for
from filmsite import db, flash, login_required
from filmsite.genres.forms import AddForm, DelForm
from filmsite.models import Movie, Director, Actor, Role, Genre

genres_blueprint = Blueprint('genres',
                               __name__,
                               template_folder='templates')

@genres_blueprint.route('/list')
def list():
    genres = Genre.query.all()
    return render_template('genres/all.html', genres=genres)


@genres_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_genre = Genre(name=name)

        db.session.add(new_genre)
        db.session.commit()

        flash("Nieuwe genre succesvol toegevoegd.")

        return redirect(url_for('genres.list'))
    return render_template('genres/create.html', form=form)


@genres_blueprint.route('/<genre_id>')
def show(genre_id):
    genre = Genre.query.filter_by(id=genre_id).first()
    movies_in_genre = [movie.movie_id for movie in genre.movies]
    movies = Movie.query.all()
    return render_template('genres/view.html', genre=genre, movies = movies, movies_in_genre=movies_in_genre)



@genres_blueprint.route('/<genre_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(genre_id):
    genre = Genre.query.filter_by(id=genre_id).first()
    form = AddForm(obj=genre)

    if form.validate_on_submit():
        genre.name=form.name.data

        db.session.add(genre)
        db.session.commit()

        flash("Genre succesvol bewerkt.")

        return redirect(url_for('genres.list'))
    return render_template('genres/edit.html', form=form)


@genres_blueprint.route('/<genre_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(genre_id):

    genre = Genre.query.filter_by(id=genre_id).first()
    form = DelForm(obj=genre)

    if form.validate_on_submit():
        db.session.delete(genre)
        db.session.commit()

        flash("Genre succesvol verwijderd.")

        return redirect(url_for('genres.list'))
    return render_template("genres/delete.html", form=form, genre=genre)
