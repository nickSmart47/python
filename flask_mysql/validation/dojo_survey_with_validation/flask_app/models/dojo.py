from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_dojo(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s); "
        result = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return result

    # @classmethod
    # def get_single_dojo(cls, data):
    #     query = "SELECT * FROM dojos WHERE id = %(id)s;"
    #     results = connectToMySQL('dojo_survey_schema').query_db(query, data)
    #     single_dojo = cls(results[0])
    #     return single_dojo

    @staticmethod
    def validate_dojo(data):
        is_valid = True

        if len(data['name']) > 50 or len(data['name']) < 2:
            is_valid = False
            flash("Name must be between 3 and 50 characters")

        if data['location'] == "-1":
            is_valid = False
            flash("Must choose a Dojo Location")

        if data['language'] == "-1":
            is_valid = False
            flash("Must choose a Favorite Language")

        if len(data['comment']) > 500 or len(data['comment']) < 3:
            is_valid = False
            flash("comment must be between 3 and 500 characters")

        return is_valid
