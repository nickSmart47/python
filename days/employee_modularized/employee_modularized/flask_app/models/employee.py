from flask_app.config.mysqlconnection import connectToMySQL

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