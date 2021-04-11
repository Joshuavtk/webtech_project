from flask import Blueprint, render_template, redirect, url_for
from filmsite import db, flash, login_required
from filmsite.movies.forms import CreateForm, DelForm
from filmsite.roles.forms import RoleForm, DelRoleForm
from filmsite.models import Movie, Director, Actor, Role

movies_blueprint = Blueprint('movies',
                               __name__,
                               template_folder='templates')


def render(name, form):
    url = 'movies/'
    return render_template(url + name + '.html', form=form)


@movies_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = CreateForm()

    directors = Director.query.all()
    directors_list=[(i.id, i.first_name + ' ' + i.last_name) for i in directors]
    form.director_id.choices = directors_list

    if form.validate_on_submit():
    
        new_movie = Movie(
            title=form.title.data, 
            release_year=form.release_year.data, 
            visitor_amount = form.visitor_amount.data,
            gross_income = form.gross_income.data,
            playtime = form.playtime.data,
            genre = form.genre.data,
            trailer_url = form.trailer_url.data,
            director_id = form.director_id.data
            )

        db.session.add(new_movie)
        db.session.commit()

        flash("Nieuwe film succesvol toegevoegd.")
        return redirect(url_for('movies.show', movie_id = new_movie.id))
    return render('create', form)


@movies_blueprint.route('/list')
def list():
    movies = Movie.query.all()
    return render_template('movies/all.html', movies=movies)


@movies_blueprint.route('/<movie_id>/delete', methods=['GET', 'POST'])
@login_required
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


@movies_blueprint.route("/<movie_id>/add_role", methods=['GET', 'POST'])
@login_required
def add_role(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    form = RoleForm()

    actors = Actor.query.all()
    actors_list=[]
    for actor in actors:
        if movie.id not in [role.movie_id for role in actor.roles]:
            actors_list.append((actor.id, actor))
    form.actor_id.choices = actors_list

    if form.validate_on_submit():

        new_role = Role(
            movie_id=movie.id, 
            actor_id=form.actor_id.data, 
            playing_as = form.playing_as.data)

        db.session.add(new_role)
        db.session.commit()

        flash("Nieuwe rol succesvol toegevoegd.")
        return redirect(url_for('movies.show', movie_id = movie.id))

    return render_template("movies/add_role.html", form=form, movie=movie)

@movies_blueprint.route("/<movie_id>/edit_role/<role_id>", methods=['GET', 'POST'])
@login_required
def edit_role(movie_id, role_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    role = Role.query.filter_by(id=role_id).first()
    form = RoleForm(obj=role)

    actors = Actor.query.all()
    actors_list=[]
    for actor in actors:
        if movie.id not in [role.movie_id for role in actor.roles] or role.actor_id == actor.id:
            actors_list.append((actor.id, actor))
    form.actor_id.choices = actors_list

    if form.validate_on_submit():

        role.movie_id=movie.id, 
        role.actor_id=form.actor_id.data, 
        role.playing_as = form.playing_as.data

        db.session.add(role)
        db.session.commit()

        flash("Rol succesvol bewerkt.")
        return redirect(url_for('movies.show', movie_id = movie.id))

    return render_template("movies/edit_role.html", form=form, movie=movie, role=role)



@movies_blueprint.route('/<movie_id>/delete_role/<role_id>', methods=['GET', 'POST'])
@login_required
def delete_role(movie_id, role_id):

    role = Role.query.filter_by(id=role_id).first()
    form = DelRoleForm(obj=role)

    if form.validate_on_submit():
        db.session.delete(role)
        db.session.commit()

        flash("Rol succesvol verwijderd.")

        return redirect(url_for('movies.show', movie_id = movie_id))
    return render('delete_role', form)


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
        movie.visitor_amount = form.visitor_amount.data
        movie.gross_income = form.gross_income.data
        movie.playtime = form.playtime.data
        movie.genre = form.genre.data
        movie.trailer_url = form.trailer_url.data

        db.session.add(movie)
        db.session.commit()

        flash("Film succesvol bijgewerkt.")
        return redirect(url_for('movies.show', movie_id = movie.id))

    return render_template("movies/edit.html", form=form, movie=movie)