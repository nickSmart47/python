from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        dojos = []
        for row in results:
            # print(row)
            if len(dojos) == 0:
                new_dojo = (cls(row))
                dojos.append(new_dojo)
            elif dojos[-1].id != row['id']:
                new_dojo = (cls(row))
                dojos.append(new_dojo)

            if row['ninjas.id'] != None:
                new_ninja_data = {
                    'id' : row['ninjas.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'age' : row['age'],
                    'dojo_id' : row['dojo_id'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at']
                }
                new_ninja = Ninja(new_ninja_data)
                new_dojo.ninjas.append(new_ninja)
                new_ninja.dojo = new_dojo

        return dojos

    @classmethod
    def create_new_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return result

    # @classmethod
    # def delete_dojo(cls, data):
    #     query = "DELETE FROM dojos WHERE id = %(id)s;"
    #     connectToMySQL('dojos_and_ninjas').query_db(query, data)
    
    @classmethod
    def get_single_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        # try/except block solves the problem of
        # showing an empty dojo with no ninjas inserted yet...
        try: 
            single_dojo = cls(results[0])
        except IndexError:
            query = "SELECT * FROM dojos WHERE id = %(id)s;"
            results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
            # print(f'single dojo is {results}')
            return results[0]
        for row in results:

            if row['ninjas.id'] != None:
                new_ninja_data = {
                    'id' : row['ninjas.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'age' : row['age'],
                    'dojo_id' : row['dojo_id'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at']
                }
                new_ninja = Ninja(new_ninja_data)
                single_dojo.ninjas.append(new_ninja)
                new_ninja.dojo = single_dojo
        # print(single_dojo.ninjas)
        return single_dojo
    
    # @classmethod
    # def update_single_dojo(cls, data):
    #     query = "UPDATE dojos SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
    #     connectToMySQL('dojos_and_ninjas').query_db(query, data)