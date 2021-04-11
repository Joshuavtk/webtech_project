from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    first_name = StringField('Voornaam regisseur:')
    last_name = StringField('Achternaam regisseur:')
    submit = SubmitField('Opslaan')

class DelForm(FlaskForm):
    submit = SubmitField('Verwijder')
