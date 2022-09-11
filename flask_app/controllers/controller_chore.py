from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_chore, model_chores_has_days, model_day

@app.route('/chore/new')          
def chore_new():
    return render_template('chore_new.html')

@app.route('/chore/create', methods=['POST'])          
def chore_create():
    print(request.form)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    data = {**request.form}
    for day in days:
        if day in request.form:
            del data[day]
    chore_id = model_chore.Chore.create(**data)
    for day in days:
        if day in request.form:
            day_id = model_day.Day.get_one(day=day).id
            model_chores_has_days.Chores_has_days.create(chore_id=chore_id, day_id=day_id)

    user_id = session['uuid']
    return redirect(f'/user/{user_id}')

@app.route('/chore/<int:id>')          
def chore_show(id):
    return render_template('chore_show.html')

@app.route('/chore/<int:id>/edit')          
def chore_edit(id):
    return render_template('chore_edit.html')

@app.route('/chore/<int:id>/update', methods=['POST'])          
def chore_update(id):
    return redirect('/')

@app.route('/chore/<int:id>/delete')          
def chore_delete(id):
    return redirect('/')
