from flask import Blueprint, render_template, redirect, url_for
from filmsite import db, flash, login_required
from filmsite.models import Director
from filmsite.directors.forms import AddForm, DelForm

directors_blueprint = Blueprint('directors',
                                __name__,
                                template_folder='templates')

url = 'directors/'

@directors_blueprint.route('/list')
def list():
    directors = Director.query.all()
    return render_template(url + 'all.html', directors=directors)


@directors_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():

    form = AddForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_director = Director(first_name=first_name, last_name=last_name)

        db.session.add(new_director)
        db.session.commit()

        flash("Nieuwe regisseur succesvol toegevoegd.")

        return redirect(url_for('directors.list'))
    return render_template(url + 'create.html', form=form)


@directors_blueprint.route("/<director_id>", methods=['GET', 'POST'])
def show(director_id):
    director = Director.query.filter_by(id=director_id).first()

    return render_template(url + "view.html", director=director)



@directors_blueprint.route("/<director_id>/edit", methods=['GET', 'POST'])
@login_required
def edit(director_id):
    director = Director.query.filter_by(id=director_id).first()
    form = AddForm(obj=director)

    if form.validate_on_submit():

        director.first_name = form.first_name.data
        director.last_name = form.last_name.data


        db.session.add(director)
        db.session.commit()

        flash("Regisseur succesvol bijgewerkt.")
        return redirect(url_for('directors.show', director_id = director.id))

    return render_template(url + "edit.html", form=form, director=director)


@directors_blueprint.route('/<director_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(director_id):

    director = Director.query.filter_by(id=director_id).first()
    form = DelForm(obj=director)

    if form.validate_on_submit():
        db.session.delete(director)
        db.session.commit()

        flash("Regisseur succesvol verwijderd.")

        return redirect(url_for('directors.list'))
    return render_template(url + "delete.html", form=form, director=director)
