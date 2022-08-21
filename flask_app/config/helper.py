from functools import wraps
from flask import g, request, redirect, url_for, session
from flask_app.models.users import model_kid, model_parent

def login_required(f):
    @wraps(f)
    def login(*args, **kwargs):
        if 'user' not in session or 'user' in session and 'uuid' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return login

def get_logged_in_user():
    user = False
    if session['user']['type'] == 'kid':
        user = model_kid.Kid.get_one(id=session['uuid'])
    elif session['user']['type'] == 'parent':
        user = model_parent.Parent.get_one(id = session['uuid'])
    return user