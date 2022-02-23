from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash
import re


class Car:

    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.seller_id = data['seller_id']
        if data['seller_name']:
            self.seller_name = data['seller_name']
        else:    
            self.seller_name = None

    @classmethod
    def create_new_car(cls, data):
        query = "INSERT INTO cars (price, model, make, year, description, seller_id) VALUES (%(price)s, %(model)s, %(make)s,  %(year)s, %(description)s, %(seller_id)s);"
        result = connectToMySQL(
            "exam_schema").query_db(query, data)
        return result

    @classmethod
    def get_car_by_id(cls, data):
        query = "SELECT * FROM cars WHERE id = %(id)s"
        results = connectToMySQL("exam_schema").query_db(query, data)
        return results[0]

    @classmethod
    def get_all_cars(cls):
        query = ("SELECT * FROM cars")
        results = connectToMySQL('exam_schema').query_db(query)
        cars = []

        for row in results:
            if row['id'] != None:
                seller_id = row['seller_id']
                seller = User.get_user_by_id(data={
                    'id': seller_id
                    })
                print( f'{seller.first_name} {seller.last_name}')
                new_car_data = {
                    'id': row['id'],
                    'price': row['price'],
                    'model': row['model'],
                    'make': row['make'],
                    'year': row['year'],
                    'description': row['description'],
                    'seller_id': row['seller_id'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at'],
                    'seller_name' : f'{seller.first_name} {seller.last_name}'
                }
            new_car = Car(new_car_data)
            cars.append(new_car)

        return cars

    @classmethod
    def update_car(cls, data):
        query = "UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s, seller_id = %(seller_id)s WHERE id = %(id)s;"
        connectToMySQL('exam_schema').query_db(query, data)

    @classmethod
    def delete_car(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s"
        results = connectToMySQL("exam_schema").query_db(query, data)       

    @staticmethod
    def validate_car_info(data):
        is_valid = True


        if len(data['price']) == 0:
            is_valid = False
            flash('Please enter a Price.')
        elif int(data['price']) > 2147483647:
            is_valid = False
            flash('Please enter a Price that is less than $2147483648')
        else:
            if int(data['price']) < 1:
                is_valid = False
                flash('Price must be greater than 0')
        
        if len(data['year']) == 0:
            is_valid = False
            flash('Please enter a Year.')
        elif int(data['year']) > 2023 or int(data['year']) < 1885:
            is_valid = False
            flash('Please enter a Year between 1885 to 2023')
        else:        
            if int(data['year']) < 1:
                is_valid = False
                flash('Year must be greater than 0')   

        if len(data['model']) == 0:
            is_valid = False
            flash('Please enter a Model.')     

        if len(data['make']) == 0:
            is_valid = False
            flash('Please enter a Make.')      

        if len(data['description']) == 0 or not re.search('[a-zA-Z]', data['description']):
            is_valid = False
            flash('Please enter a Description.')           

        return is_valid