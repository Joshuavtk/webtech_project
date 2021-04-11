from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms import StringField, IntegerField, SubmitField
from filmsite.models import Director

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

    visitor_amount = wtforms.IntegerField(
        "Aantal bezoekers", validators=[DataRequired()],
        render_kw={'placeholder': 'Aantal...'}
    )

    gross_income = wtforms.IntegerField(
        "Opbrengst", validators=[DataRequired()],
        render_kw={'placeholder': 'Opbrengst...'}
    )

    playtime = wtforms.IntegerField(
        "Speelduur", validators=[DataRequired()],
        render_kw={'placeholder': 'Lengte...'}
    )

    genre = wtforms.StringField(
        "Genre", validators=[DataRequired()],
        render_kw={'placeholder': 'Genre...'}
    )

    trailer_url = wtforms.StringField(
        "Trailer url (youtube link)", validators=[DataRequired()],
        render_kw={'placeholder': 'Url...'}
    )

    director_id = wtforms.SelectField(
        "Kies een regisseur", validators=[DataRequired()], coerce=int
    )

    submit = wtforms.SubmitField("Opslaan")