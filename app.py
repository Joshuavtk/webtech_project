from filmsite import app
from flask import render_template
from filmsite import login_manager
from filmsite.models import User, Genre

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    genres = Genre.query.all()
    return render_template('home.html', genres=genres)

if __name__ == '__main__':
    app.run(debug=True)