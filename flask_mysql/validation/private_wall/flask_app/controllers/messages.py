from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/send/message/<int:user_id>/<int:other_user_id>', methods =["POST"])
def send_message(user_id, other_user_id):
    data = {
        'message' : request.form['message'],
        'creator_id' : user_id,
    }
    Message.create_message(data)
    message_id = Message.get_message_id(data)
    print (message_id)
    data = {
        'recipient_id' : other_user_id,
        'message_id' : message_id['id']
    }
    Message.send_message(data)
    return redirect('/dashboard')