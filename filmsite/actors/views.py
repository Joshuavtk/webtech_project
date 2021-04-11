from flask import Blueprint, render_template, redirect, url_for
from filmsite import db, flash, login_required
from filmsite.models import Actor
from filmsite.actors.forms import AddForm, DelForm

actors_blueprint = Blueprint('actors',
                                __name__,
                                template_folder='templates/actors')


@actors_blueprint.route('/list')
def list():
    actors = Actor.query.all()
    return render_template('all.html', actors=actors)


@actors_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():

    form = AddForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_actor = Actor(first_name=first_name, last_name=last_name)

        db.session.add(new_actor)
        db.session.commit()

        flash("Nieuwe acteur succesvol toegevoegd.")

        return redirect(url_for('actors.list'))
    return render_template('create.html', form=form)


@actors_blueprint.route("/<actor_id>", methods=['GET', 'POST'])
def show(actor_id):
    actor = Actor.query.filter_by(id=actor_id).first()

    return render_template("view.html", actor=actor)



@actors_blueprint.route("/<actor_id>/edit", methods=['GET', 'POST'])
@login_required
def edit(actor_id):
    actor = Actor.query.filter_by(id=actor_id).first()
    form = AddForm(obj=actor)

    if form.validate_on_submit():

        actor.first_name = form.first_name.data
        actor.last_name = form.last_name.data


        db.session.add(actor)
        db.session.commit()

        flash("Acteur succesvol bijgewerkt.")
        return redirect(url_for('actors.show', actor_id = actor.id))

    return render_template("edit.html", form=form, actor=actor)


@actors_blueprint.route('/<actor_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(actor_id):

    actor = Actor.query.filter_by(id=actor_id).first()
    form = DelForm(obj=actor)

    if form.validate_on_submit():
        db.session.delete(actor)
        db.session.commit()

        flash("Acteur succesvol verwijderd.")

        return redirect(url_for('actors.list'))
    return render_template("delete.html", form=form, actor=actor)
