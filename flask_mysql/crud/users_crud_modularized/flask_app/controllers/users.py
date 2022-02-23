from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.user import User

@app.route('/') # list all users
def index():
    all_users = User.get_all_users()
    return render_template('index.html', users = all_users)

@app.route('/users/create')
def create():
    return render_template('create.html')

@app.route('/users/create_new_user', methods = ['POST'])
def create_new_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.create_new_user(data)
    return redirect('/')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id' : user_id
    }
    User.delete_user(data)
    return redirect('/')

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        'id' : user_id
    }
    user = User.get_single_user(data)
    return render_template('edit_user.html', user = user)

@app.route('/users/<int:user_id>/update', methods = ['POST'])
def update_user(user_id):
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : user_id
    }
    User.update_single_user(data)
    return redirect(url_for('show_user', user_id = user_id))

@app.route('/users/<int:user_id>/show')
def show_user(user_id):
    data = {
        'id' : user_id
    }
    user = User.get_single_user(data)
    return render_template('show_user.html', user = user)