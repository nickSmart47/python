from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/dojos')
    
@app.route('/dojos') # list all dojos
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos = all_dojos)

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id' : dojo_id
    }
    dojo = Dojo.get_single_dojo(data)
    return render_template('show_dojo.html', dojo = dojo)


@app.route('/ninjas')
def create_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template('create_ninja.html', dojos = all_dojos)

@app.route('/ninjas/create_new_ninja', methods = ['POST'])
def create_new_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    new_ninja_dojo_id = request.form['dojo_id']
    Ninja.create_new_ninja(data)
    return redirect(url_for('show_dojo', dojo_id = new_ninja_dojo_id))



@app.route('/dojos/create_new_dojo', methods = ['POST'])
def create_new_dojo():
    data = {
        'name' : request.form['dojo_name'],
    }
    Dojo.create_new_dojo(data)
    return redirect('/')

# @app.route('/dojos/<int:dojo_id>/delete')
# def delete_dojo(dojo_id):
#     data = {
#         'id' : dojo_id
#     }
#     dojo.delete_dojo(data)
#     return redirect('/')

# @app.route('/dojos/<int:dojo_id>/edit')
# def edit_dojo(dojo_id):
#     data = {
#         'id' : dojo_id
#     }
#     dojo = dojo.get_single_dojo(data)
#     return render_template('edit_dojo.html', dojo = dojo)

# @app.route('/dojos/<int:dojo_id>/update', methods = ['POST'])
# def update_dojo(dojo_id):
#     data = {
#         'first_name' : request.form['first_name'],
#         'last_name' : request.form['last_name'],
#         'email' : request.form['email'],
#         'id' : dojo_id
#     }
#     dojo.update_single_dojo(data)
#     return redirect(url_for('show_dojo', dojo_id = dojo_id))

