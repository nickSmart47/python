from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'super secret survey time'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def results():
    print(request.form)
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return render_template('results.html',
    name = session['name'],
    dojo_location = session['dojo_location'],
    favorite_language = session['favorite_language'],
    comment = session['comment'])


if __name__ == '__main__':
    app.run(debug=True)