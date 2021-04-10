from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    naam = StringField('Naam student:')
    doc_id = IntegerField("Id van de docent: ")
    submit = SubmitField('Voeg toe')
