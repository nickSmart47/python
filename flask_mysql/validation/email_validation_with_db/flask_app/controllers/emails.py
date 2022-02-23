from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.email import Email


@app.route('/')  # list all emails
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_email():
    data = {
        'email': request.form['email'],
    }
    if Email.validate_email(data):
        Email.create_email(data)
        return redirect('/success')
    else:
        return redirect('/')
        

@app.route('/success')
def success():
    all_emails = Email.get_all_emails()
    return render_template('success.html', emails = all_emails)

@app.route('/delete/<int:email_id>')
def delete_email(email_id):
    data = {
        'id' : email_id
    }
    Email.delete_email(data)
    return redirect('/success')