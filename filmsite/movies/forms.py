from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms import StringField, IntegerField, SubmitField
from filmsite.models import Director

# class AddForm(FlaskForm):
#     naam = StringField('Naam docent:')
#     submit = SubmitField('Voeg toe')

class DelForm(FlaskForm):
    submit = SubmitField('Verwijder')

class CreateForm(FlaskForm):
    title = wtforms.StringField(
        "Titel film",
        validators=[DataRequired()],
        render_kw={'placeholder': 'Titel...'}
    )

    release_year = wtforms.IntegerField(
        "Jaar van uitgave", validators=[DataRequired()],
        render_kw={'placeholder': 'Jaar...'}
    )

    director_id = wtforms.SelectField(
        "Kies een directeur", validators=[DataRequired()], coerce=int
    )

    submit = wtforms.SubmitField("Opslaan")