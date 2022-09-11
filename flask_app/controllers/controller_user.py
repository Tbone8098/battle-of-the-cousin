from flask_app import app, bcrypt
from flask import render_template, redirect, session, request

from flask_app.models.users import model_user, model_family, model_rent, model_kiddo
from flask_app.models import model_difficulty

@app.route('/user/new')          
def user_new():
    return render_template('user_new.html')

@app.route('/user/logout')          
def user_logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/login', methods=['POST'])
def user_login():
    potential_login = model_rent.Rent.get_one(email=request.form['login_cred'])
    if not potential_login:
        potential_login = model_kiddo.Kiddo.get_one(battlename=request.form['login_cred'])
        if not potential_login:
            return redirect('/')
    user = model_user.User.get_one(id=potential_login.user_id)
    if not bcrypt.check_password_hash(user.get_pw, request.form['pw']):
        return redirect('/')
    session['uuid'] = user.id
    session['family_id'] = user.family_id
    return redirect('/')

@app.route('/user/create', methods=['POST'])          
def user_create():
    model_user.User.create_user(**request.form)
    user_id = session['uuid']
    if 'landing' in request.form:
        return redirect('/')
    return redirect(f'/user/{user_id}')

@app.route('/user/<int:id>')          
@app.route('/user/<int:id>/<subpage>')          
def user_show(id, subpage = 'chore_settings'):
    context = {
        'user': model_user.User.get_one(id=session['uuid']),
        'all_difficulties': model_difficulty.Difficulty.get_all(),
        'subpage': subpage
    }
    return render_template('user_show.html', **context)

@app.route('/user/<int:id>/edit')          
def user_edit(id):
    return render_template('user_edit.html')

@app.route('/user/<int:id>/update', methods=['POST'])          
def user_update(id):
    return redirect('/')

@app.route('/user/<int:id>/delete')          
def user_delete(id):
    return redirect('/')
