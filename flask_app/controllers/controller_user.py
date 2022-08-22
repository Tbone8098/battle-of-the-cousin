from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.users import model_user, model_family, model_rent

@app.route('/user/new')          
def user_new():
    return render_template('user_new.html')

@app.route('/user/logout')          
def user_logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/create', methods=['POST'])          
def user_create():
    print("**********")
    print(request.form)
    family_id = model_family.Family.create(**request.form)
    if not family_id:
        return redirect('/')
    data = {
        **request.form,
        'family_id': family_id,
        'level': 1,
    }
    user_id = model_user.User.create(**data)
    if not user_id:
        return redirect('/')
    data['user_id'] = user_id
    model_rent.Rent.create(**data)
    session['uuid'] = user_id
    return redirect('/')

@app.route('/user/<int:id>')          
def user_show(id):
    return render_template('user_show.html')

@app.route('/user/<int:id>/edit')          
def user_edit(id):
    return render_template('user_edit.html')

@app.route('/user/<int:id>/update', methods=['POST'])          
def user_update(id):
    return redirect('/')

@app.route('/user/<int:id>/delete')          
def user_delete(id):
    return redirect('/')
