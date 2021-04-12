from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms import StringField, IntegerField, SubmitField, widgets, SelectMultipleField
from filmsite.models import Director

class DelForm(FlaskForm):
    submit = SubmitField('Verwijder')

class MultiCheckboxField(SelectMultipleField):
    # def __init__(genres):
    #     self.genres = genres

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
    # option_widget = widgets.Select(multiple=True)
    # def iter_choices(genres):
    #     return [(1,2,3)]

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

    trailer_url = wtforms.StringField(
        "Trailer url (youtube link)", validators=[DataRequired()],
        render_kw={'placeholder': 'Url...'}
    )

    director_id = wtforms.SelectField(
        "Kies een regisseur", validators=[DataRequired()], coerce=int
    )

    genres = MultiCheckboxField('Kies genres', coerce=int)
    # genres = SelectMultipleField(coerce=int, widget=MultiCheckboxField)

    submit = wtforms.SubmitField("Opslaan")
    