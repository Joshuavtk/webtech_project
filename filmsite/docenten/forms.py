from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    naam = StringField('Naam docent:')
    submit = SubmitField('Voeg toe')

class DelForm(FlaskForm):
    id = IntegerField('Vul het ID in van de docent die verwijderd gaat worden:')
    submit = SubmitField('Verwijder')
