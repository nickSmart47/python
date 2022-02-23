from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
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
        print('user passes validation!')
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
        print('user failed validation!')
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_user_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    print(session['user_id'])
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')
    data = {
        "id" : session['user_id']
    }
    current_user = User.get_user_recipes(data)
    return render_template('dashboard.html', user = current_user)

@app.route('/logout')
def logout():
    session.clear()
    flash("Successfully logged out!")
    return redirect('/')
