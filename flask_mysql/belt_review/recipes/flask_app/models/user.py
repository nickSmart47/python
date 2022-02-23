from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.recipe import Recipe
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL(
            "recipes_schema").query_db(query, data)
        return result

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(
            "recipes_schema").query_db(query, data)
        # Didn't find a matching user
        if len(result) == 0:
            return None
        return cls(result[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(
            "recipes_schema").query_db(query, data)
        # Didn't find a matching user
        if len(result) == 0:
            return None
        return cls(result[0])

    @staticmethod
    def validate_user_info(data):
        is_valid = True

        if len(data['first_name']) < 3 or not data['first_name'].isalpha():
            is_valid = False
            flash("First Name must be at least 2 characters and consist only of letters")
        

        if len(data['last_name']) < 3 or not data['last_name'].isalpha():
            is_valid = False
            flash("Last Name must be at least 2 characters and consist only of letters")

        if len(data['email']) == 0:
            is_valid = False
            flash("Invalid email address!", 'email')
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'email')
            is_valid = False
        else:
            if User.get_user_by_email(data) != None:
                print(
                    f"output of email validation is {User.get_user_by_email(data)}")
                is_valid = False
                flash("Email address is already in use.")

        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters long.")

        if data['password'] != data['password_confirmation']:
            is_valid = False
            flash("Password Confirmation must match Password.")
        


        return is_valid


    @classmethod
    def get_user_recipes(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE user_id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        try: 
            single_user = cls(results[0])
        except IndexError:
            query = "SELECT * FROM users WHERE id = %(id)s;"
            results = connectToMySQL('recipes_schema').query_db(query, data)
            # print(f'single user is {results}')
            return results[0]
        for row in results:

            if row['recipes.id'] != None:
                new_recipe_data = {
                    'id' : row['recipes.id'],
                    'name' : row['name'],
                    'under_thirty' : row['under_thirty'],
                    'description' : row['description'],
                    'instructions' : row['instructions'],
                    'date_made' : row['date_made'],
                    'user_id' : row['user_id'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at']
                }
                new_recipe = Recipe(new_recipe_data)
                single_user.recipes.append(new_recipe)
                new_recipe.user = single_user
        # print(single_user.recipes)
        return single_user