from flask import Blueprint, render_template, redirect, url_for
from filmsite import db
from filmsite.models import Student
from filmsite.studenten.forms import AddForm

studenten_blueprint = Blueprint('studenten',
                                __name__,
                                template_folder='../templates/studenten')


@studenten_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        naam = form.naam.data
        doc_id = form.doc_id.data
        new_student = Student(naam, doc_id)
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('docenten.list'))
    return render_template('create.html', form=form)
