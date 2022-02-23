from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'secret counting key woooo'


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    print(session['visits'])
    return render_template('index.html', visits=session['visits'])


@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    if 'visits' in session:
        session.pop('visits')
    return redirect('/')


@app.route('/plus_two', methods=['POST'])
def plus_two():
    if 'visits' in session:
        session['visits'] += 1
    return redirect('/')

@app.route('/variable_counter', methods=['POST'])
def variable_counter():
    if 'visits' in session:
        session['visits'] += int(request.form['number']) - 1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
