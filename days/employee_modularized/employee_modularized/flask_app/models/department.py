from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.employee import Employee

class Department:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.employees = []

    @classmethod
    def get_all_departments(cls):
        query = "SELECT * FROM departments LEFT JOIN employees ON departments.id = employees.department_id;"

        results = connectToMySQL('employee_schema').query_db(query)

        departments = []
        for row in results:
            # print(row)
            # either create a new Department instance
            # or continue using the last one
            if len(departments) == 0:
                new_department = cls(row)
                departments.append(new_department)
            elif departments[-1].id != row['id']:
                new_department = cls(row)
                departments.append(new_department)
            # now determine if employee exists

            
            if row['employees.id'] != None:
                new_employee_data = {
                    'id' : row['employees.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'salary' : row['salary'],
                    'department_id' : row['department_id'],
                    'created_at' : row['employees.created_at'],
                    'updated_at' : row['employees.updated_at']
                }
                new_employee = Employee(new_employee_data)
                new_department.employees.append(new_employee)
                new_employee.department = new_department
                print(new_employee.first_name)

        return departments

    @classmethod
    def create_new_department(cls, data):
        query = "INSERT INTO departments (name, location) VALUES (%(name)s, %(location)s);"
        result = connectToMySQL('employee_schema').query_db(query, data)
        return result

    @classmethod
    def delete_department(cls, data):
        query = "DELETE FROM departments WHERE id = %(id)s;"
        connectToMySQL('employee_schema').query_db(query, data)

    @classmethod
    def get_single_department(cls, data):
        query = "SELECT * FROM departments WHERE id = %(id)s;"
        results = connectToMySQL('employee_schema').query_db(query, data)
        single_department = cls(results[0])
        return single_department

    @classmethod
    def update_single_department(cls, data):
        query = 'UPDATE departments SET name = %(name)s, location = %(location)s WHERE id = %(id)s;'
        connectToMySQL('employee_schema').query_db(query, data)
