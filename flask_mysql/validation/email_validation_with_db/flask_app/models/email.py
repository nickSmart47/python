from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails;"

        results = connectToMySQL('emails_schema').query_db(query)

        emails = []
        for row in results:
            emails.append(cls(row))
        return emails

    @classmethod
    def create_email(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        result = connectToMySQL('emails_schema').query_db(query, data)
        return result

    @classmethod
    def delete_email(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        connectToMySQL('emails_schema').query_db(query, data)
    
    @staticmethod
    def validate_email(data):
        is_valid = True
        
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'email')
            is_valid = False
        for email in Email.get_all_emails():  
            if data['email'] == email.email:
                flash("Email Address is already taken!", 'email_taken')
                is_valid = False

        return is_valid
