from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms import StringField, IntegerField, SubmitField
from filmsite.models import Director

class DelRoleForm(FlaskForm):
    submit = SubmitField('Verwijder')

class RoleForm(FlaskForm):
    playing_as = wtforms.StringField(
        "Naam rol",
        validators=[DataRequired()],
        render_kw={'placeholder': 'Rol...'}
    )

    actor_id = wtforms.SelectField(
        "Kies een acteur", validators=[DataRequired()], coerce=int
    )

    submit = wtforms.SubmitField("Opslaan")