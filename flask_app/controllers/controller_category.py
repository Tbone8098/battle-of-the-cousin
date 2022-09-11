from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_category

@app.route('/category/new')          
def category_new():
    return render_template('category_new.html')

@app.route('/category/create', methods=['POST'])          
def category_create():
    print(session)
    data = {
        **request.form,
        'family_id': session['family_id']
    }
    model_category.Category.create(**data)
    user_id = session['uuid']
    return redirect(f'/user/{user_id}/chore_settings')

@app.route('/category/<int:id>')          
def category_show(id):
    return render_template('category_show.html')

@app.route('/category/<int:id>/edit')          
def category_edit(id):
    return render_template('category_edit.html')

@app.route('/category/<int:id>/update', methods=['POST'])          
def category_update(id):
    return redirect('/')

@app.route('/category/<int:id>/delete')          
def category_delete(id):
    model_category.Category.delete_one(id=id)
    user_id = session['uuid']
    return redirect(f'/user/{user_id}/config')
