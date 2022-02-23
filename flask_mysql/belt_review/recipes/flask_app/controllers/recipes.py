from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from datetime import datetime



@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')

    return render_template('create_recipe.html')

@app.route('/recipes/create_new', methods = ["POST"])
def create_recipe():
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')

    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'under_thirty' : request.form['under_thirty'],
        'user_id' : session['user_id']
        }
    
    if Recipe.validate_recipe(data):
        Recipe.create_recipe(data)
        return redirect('/dashboard')
    else:
        print(data)
        return redirect('/recipes/new')

@app.route('/recipes/<int:recipe_id>')
def view_recipe(recipe_id):
    data = {
        'id' : recipe_id
    }
    recipe = Recipe.get_single_recipe(data)
    user = User.get_user_by_id(data = {
        'id' : session['user_id']
    })
    # print(recipe)
    return render_template('view_recipe.html', recipe = recipe, user = user)

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    data = {
        'id' : recipe_id
    }
    Recipe.delete_recipe(data)
    user = User.get_user_by_id(data = {
        'id' : session['user_id']
    })
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    data = {
        'id' : recipe_id
    }
    recipe = Recipe.get_single_recipe(data)
    user = User.get_user_by_id(data = {
        'id' : session['user_id']
    })
    date_made =(recipe['date_made'].strftime('%Y-%m-%d'))
    return render_template('/edit_recipe.html', recipe = recipe, user = user, date_made=date_made)

@app.route('/recipes/update/<int:recipe_id>', methods = ["POST"])
def update_recipe(recipe_id):
    if 'user_id' not in session:
        flash("This page is only available after logging in.")
        return redirect('/')

    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'under_thirty' : request.form['under_thirty'],
        'user_id' : session['user_id'],
        'id' : recipe_id
        }
    
    if Recipe.validate_recipe(data):
        Recipe.update_recipe(data)
        return redirect('/dashboard')
    else:
        return redirect('/recipes/new')