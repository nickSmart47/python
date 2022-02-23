from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.car import Car
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register/user', methods=['POST'])
def register():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "password_confirmation": request.form['password_confirmation']
    }
    if User.validate_user_info(data):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        new_user_data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash,
        }
        new_user = User.register_user(new_user_data)
        session['user_id'] = new_user
        return redirect('/dashboard')
    else:
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_user_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['user_first_name'] = user_in_db.first_name
    return redirect("/dashboard")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')
    current_user = User.get_user_by_id(data={
        "id": session['user_id']
    })
    cars = Car.get_all_cars()
    return render_template('dashboard.html', user=current_user, cars=cars)


@app.route('/logout')
def logout():
    [session.pop(key) for key in list(session.keys())]
    flash("Successfully logged out!")
    return redirect('/')
