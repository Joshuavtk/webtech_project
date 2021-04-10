from flask import Blueprint, render_template, redirect, url_for
from mijnproject import db
from mijnproject.docenten.forms import AddForm, DelForm
from mijnproject.models import Docent

docenten_blueprint = Blueprint('docenten',
                               __name__,
                               template_folder='templates')


@docenten_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        naam = form.naam.data

        new_doc = Docent(naam)
        db.session.add(new_doc)
        db.session.commit()

        return redirect(url_for('docenten.list'))

    return render_template('docenten/create.html', form=form)


@docenten_blueprint.route('/list')
def list():
    docenten = Docent.query.all()
    return render_template('list.html', docenten=docenten)


@docenten_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        doc = Docent.query.get(id)
        db.session.delete(doc)
        db.session.commit()

        return redirect(url_for('docenten.list'))
    return render_template('delete.html', form=form)
