from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under_thirty = data['under_thirty']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, under_thirty, description, instructions, date_made, user_id) VALUES (%(name)s, %(under_thirty)s, %(description)s, %(instructions)s, %(date_made)s, %(user_id)s);"
        result = connectToMySQL(
            "recipes_schema").query_db(query, data)
        return result

    @classmethod
    def get_single_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL("recipes_schema").query_db(query, data)
        return results[0]
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        results = connectToMySQL("recipes_schema").query_db(query, data)
    
    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_thirty = %(under_thirty)s WHERE id = %(id)s;"
        connectToMySQL('recipes_schema').query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 4 :
            is_valid = False
            flash("Name must be at least 3 characters.")
        
        if len(data['description']) < 4 :
            is_valid = False
            flash("Description must be at least 3 characters.")

        if len(data['instructions']) < 4 :
            is_valid = False
            flash("Instructions must be at least 3 characters.")
        
        if data['date_made'] == '':
            is_valid = False
            flash("Please choose a Date Made")

        if data['under_thirty'] == None:
            is_valid = False
            flash("Please choose whether recipe can be made in under 30 minutes")

        return is_valid