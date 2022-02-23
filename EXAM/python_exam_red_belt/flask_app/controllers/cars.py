from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.car import Car


@app.route('/new')
def new_car():
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')
    return render_template('create_car.html')


@app.route('/new/car_for_sale/<int:seller_id>', methods=["POST"])
def create_new_car(seller_id):
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')
    data = {
        'price': request.form['price'],
        'model': request.form['model'],
        'make': request.form['make'],
        'year': request.form['year'],
        'description': request.form['description'],
        'seller_id': seller_id
    }
    if Car.validate_car_info(data):
        new_car = Car.create_new_car(data)
        return redirect(f'/show/{new_car}')
    else:
        return redirect('/new')


@app.route('/show/<int:car_id>')
def show_car(car_id):
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    current_user = User.get_user_by_id(data)
    car = Car.get_car_by_id(data = {
        'id': car_id
    })
    seller_id = car['seller_id']
    seller = User.get_user_by_id(data = {
        'id': seller_id
    })
    return render_template('show_car.html',
                           car=car,
                           user=current_user,
                           seller=seller)


@app.route('/delete/<int:car_id>')
def delete_car(car_id):
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')
    data = {
        'id' : car_id
    }
    Car.delete_car(data)
    return redirect('/dashboard')

@app.route('/edit/<int:car_id>')
def edit_car(car_id):
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')
    car = Car.get_car_by_id(data = {
        'id' : car_id})
    if car['seller_id'] != session['user_id']:
        flash("You must be the owner of the car you wish to edit.")
        return redirect('/dashboard')
    
    return render_template('edit_car.html', car=car)

@app.route('/update/<int:car_id>/<int:seller_id>', methods = ["POST"])
def update_car(car_id, seller_id):
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')
    data = {
        'id' : car_id,
        'price': request.form['price'],
        'model': request.form['model'],
        'make': request.form['make'],
        'year': request.form['year'],
        'description': request.form['description'],
        'seller_id': seller_id
    }
    if Car.validate_car_info(data):
        Car.update_car(data)
        return redirect('/dashboard')
    else:
        return redirect(f'/edit/{car_id}') 