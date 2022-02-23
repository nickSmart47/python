from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }
    if Dojo.validate_dojo(data):
        Dojo.create_new_dojo(data)
        return render_template('result.html',
                               name=data['name'],
                               location=data['location'],
                               language=data['language'],
                               comment=data['comment'])
    else:
        return redirect('/')
