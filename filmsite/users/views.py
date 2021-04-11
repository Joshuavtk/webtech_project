from filmsite import app, login_user, logout_user, login_required, current_user, redirect, url_for, flash, db, render_template
from filmsite.users.forms import CreateAccountForm, SignInForm
from filmsite.models import User
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask import Blueprint

users_blueprint = Blueprint('users',
                               __name__,
                               template_folder='templates')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = CreateAccountForm()
    if form.validate_on_submit():
        user_email = User.query.filter_by(
            user_email=form.user_email.data).first()
        if user_email is not None:
            flash("Failed creating account, email already in use.")
            return redirect(url_for("register"))

        new_user = User(
            user_name=form.user_name.data,
            user_email=form.user_email.data,
            user_password=form.user_password.data,
            creation_date=datetime.datetime.now()
        )
        new_user.user_password = generate_password_hash(new_user.user_password)

        db.session.add(new_user)
        db.session.commit()
        flash("Created account successfully.")

        login_user(new_user)
        flash("Signed in successfully.")
        return redirect(url_for("index"))

    return render_template("users/register.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = SignInForm()
    if form.validate_on_submit():
        user_email = User.query.filter_by(
            user_email=form.user_email.data).first()
        if user_email is None:
            flash("Invalid user.")
            return redirect(url_for('login'))
        elif not user_email.check_password(form.user_password.data):
            flash("Invalid password.")
            return redirect(url_for('login'))

        login_user(user_email)
        flash("Signed in successfully.")
        return redirect(url_for("index"))

    return render_template("users/login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Signed out successfully.")
    return redirect(url_for("index"))
