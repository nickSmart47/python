from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Message:

    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator_id = None

    @classmethod
    def get_user_messages(cls, data):
        pass

    @classmethod
    def create_message(cls, data):
        query = "INSERT INTO messages (text, creator_id) values (%(message)s, %(creator_id)s);"
        connectToMySQL("private_wall_schema").query_db(query, data)

    @classmethod   
    def send_message(cls, data):    
        query = "INSERT INTO message_recipient (recipient_id, message_id) VALUES (%(recipient_id)s, %(message_id)s);"
        result = connectToMySQL("private_wall_schema").query_db(query, data)
        return result

    @classmethod
    def get_message_id(cls, data):
        query = "SELECT id FROM messages WHERE text = %(message)s"
        result = connectToMySQL("private_wall_schema").query_db(query, data)

        return result[0]