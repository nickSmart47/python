from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "whatever you want"
# routes go here
# GET - a GET request, for data from the server
# POST - a POST request, when we send data to the server (typically via a form)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_information', methods=["POST"])
def handle_information():
    session['maiden_name'] = request.form['maiden_name']
    session['first_pet_name'] = request.form['first_pet_name']
    session['social_security_number'] = request.form['social_security_number']
    return redirect('/form_result')

    # print(request.form['maiden_name'])
    # return render_template('results.html',
    # maiden_name = request.form['maiden_name'],
    # pet_name = request.form['first_pet_name'],
    # ssn = request.form['social_security_number']
    # ) # Don't do this! if user bookmarks they will have problems
    # Try not to render on a POST request!!!

@app.route('/form_result')
def form_result():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)

