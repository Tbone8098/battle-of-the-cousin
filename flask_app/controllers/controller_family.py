from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.users import model_family

@app.route('/family/new')          
def family_new():
    return render_template('family_new.html')

@app.route('/family/create', methods=['POST'])          
def family_create():
    return redirect('/')

@app.route('/family/<int:id>')          
def family_show(id):
    return render_template('family_show.html')

@app.route('/family/<int:id>/edit')          
def family_edit(id):
    return render_template('family_edit.html')

@app.route('/family/<int:id>/update', methods=['POST'])          
def family_update(id):
    return redirect('/')

@app.route('/family/<int:id>/delete')          
def family_delete(id):
    return redirect('/')
