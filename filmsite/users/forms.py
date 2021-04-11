from filmsite import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Length, EqualTo, Email

class CreateAccountForm(FlaskForm):
    user_name = wtforms.StringField(
        "Username",
        validators=[DataRequired(),
                    Length(1, 64, message="Username must be less than 64 characters long.")],
        render_kw={'placeholder': 'Username'}
    )

    user_email = wtforms.StringField(
        "E-Mail",
        validators=[DataRequired(),
                    Email(message=None),
                    Length(3, 320)],
        render_kw={'placeholder': 'example@gmail.com'}
    )

    user_password = wtforms.PasswordField(
        "Password", validators=[DataRequired()],
        render_kw={'placeholder': 'Password'}
    )

    user_password_repeat = wtforms.PasswordField(
        "Repeat Password", 
        validators=[
            DataRequired(),
            EqualTo("user_password", message="Passwords do not match.")
        ],
        render_kw={'placeholder': 'Repeat Password'}
    )

    submit_register = wtforms.SubmitField("Create Account")


class SignInForm(FlaskForm):
    user_email = wtforms.StringField(
        "E-Mail",
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'example@gmail.com'}
    )

    user_password = wtforms.PasswordField(
        "Password", validators=[DataRequired()],
        render_kw={'placeholder': 'Password'}
    )

    submit_login = wtforms.SubmitField("Sign In")
