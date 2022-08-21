from flask_app import app, bcrypt
from flask import render_template, redirect, session, request

from flask_app.models.users import model_user, model_family, model_kid, model_parent

@app.route('/user/logout')          
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/login', methods=['POST'])
def login():
    user = model_parent.Parent.get_one(email=request.form['username'])
    if user:
        if not bcrypt.check_password_hash(user.pw, request.form['pw']):
            return redirect('/')

        session['uuid'] = user.id
        session['user'] = {
            'type': 'parent'
        }
    else:
        user = model_kid.Kid.get_one(username=request.form['username'])
        if not user:
            print("No user found")
            return redirect('/')
        session['uuid'] = user.id
        session['user'] = {
            'type': 'kid'
        }
    return redirect('/')

@app.route('/user/create', methods=['POST'])          
def user_create():
    print("*"*80)
    print(request.form)
    print("*"*80)

    if (request.form['user_type'] != 'parent' and request.form['user_type'] != 'child'):
        return redirect('/')

    
    # determine user type
    data = {**request.form}
    if request.form['user_type'] == 'parent':

        # if no family code is given
        if request.form['family_code'] == '':
            family_id = model_family.Family.create(**data)
            data['family_id'] = family_id
            data['is_parent'] = True

            user_id = model_user.User.create(**data)

            data['user_id'] = user_id
            parent_id = model_parent.Parent.create(**data)

            session['uuid'] = parent_id
            session['user'] = {
                'type': 'parent'
            }
            return redirect('/')

            
    elif request.form['user_type'] == 'child':
        family_id = model_family.Family.get_one(code=request.form['family_code']).id
        data['family_id'] = family_id
        data['is_parent'] = False
        user_id = model_user.User.create(**data)
        data['user_id'] = user_id
        kid_id = model_kid.Kid.create(**data)
        session['uuid'] = kid_id
        session['user'] = {
            'type': 'kid'
        }

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
