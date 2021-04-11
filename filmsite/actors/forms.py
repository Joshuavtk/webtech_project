from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    first_name = StringField('Voornaam acteur:')
    last_name = StringField('Achternaam acteur:')
    submit = SubmitField('Opslaan')

class DelForm(FlaskForm):
    submit = SubmitField('Verwijder')
