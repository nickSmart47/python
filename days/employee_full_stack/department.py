from mysqlconnection import connectToMySQL


class Department:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_departments(cls):
        query = "SELECT * FROM departments;"

        results = connectToMySQL('employee_schema').query_db(query)

        departments = []
        for row in results:
            departments.append(cls(row))
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
        result = connectToMySQL('employee_schema').query_db(query, data)
        single_department = cls(result[0])
        return single_department

    @classmethod
    def update_single_department(cls, data):
        query = "UPDATE departments SET name = %(name)s, location = %(location)s WHERE id = %(id)s"
        connectToMySQL('employee_schema').query_db(query, data)
