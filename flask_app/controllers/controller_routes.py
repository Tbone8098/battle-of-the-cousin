from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.config.helper import get_logged_in_user
from flask_app.models.users import model_user

@app.route('/')          
def index():
    print(session)
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')          
def dashboard():
    print(session)
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'user': get_logged_in_user()
    }
    return render_template('dashboard.html', **context)

# @app.errorhandler(404)
# def server_error(e):
#     print('running error function')
#     return render_template('404.html')