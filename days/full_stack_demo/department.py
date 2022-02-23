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
        query = 'SELECT * FROM departments;'

        results = connectToMySQL('employee_schema').query_db(query)

        departments = []
        for item in results:
            departments.append(Department(item)) #can append with cls(item) or name of class (which is Department)
        return departments