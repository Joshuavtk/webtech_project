from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Naam genre:')
    submit = SubmitField('Opslaan')

class DelForm(FlaskForm):
    submit = SubmitField('Verwijder')
