from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_arena

@app.route('/arena/new')          
def arena_new():
    return render_template('arena_new.html')

@app.route('/arena/create', methods=['POST'])          
def arena_create():
    return redirect('/')

@app.route('/arena/<int:id>')          
def arena_show(id):
    return render_template('arena_show.html')

@app.route('/arena/<int:id>/edit')          
def arena_edit(id):
    return render_template('arena_edit.html')

@app.route('/arena/<int:id>/update', methods=['POST'])          
def arena_update(id):
    return redirect('/')

@app.route('/arena/<int:id>/delete')          
def arena_delete(id):
    return redirect('/')
