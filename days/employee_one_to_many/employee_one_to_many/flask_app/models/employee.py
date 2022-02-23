from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Employee:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.salary = data['salary']
        self.department_id = data['department_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.department = None

    @classmethod
    def create_new_employee(cls, data):
        query = "INSERT INTO employees (first_name, last_name, salary, department_id) VALUES (%(first_name)s, %(last_name)s, %(salary)s, %(department_id)s);"
        result = connectToMySQL('employee_schema').query_db(query, data)
        return result

    @staticmethod
    def validate_employee(data):
        is_valid = True

        if len(data['first_name']) > 50 or len(data['first_name']) < 2:
            is_valid = False
            flash("Employee first name must be 2 to 50 characters long")

        if len(data['last_name']) > 50 or len(data['last_name']) < 2:
            is_valid = False
            flash("Employee last name must be 2 to 50 characters long")

        try:
            new_salary = int(data['salary'])
            if new_salary < 40000 or new_salary > 200000:
                is_valid = False
                flash("Employee salary should be a number between 40000 and 200000")
        except:
            is_valid = False
            flash("Employee salary should be a number between 40000 and 200000")

        return is_valid

