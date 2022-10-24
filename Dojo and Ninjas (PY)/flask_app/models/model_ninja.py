# import the function that will return an instance of a connection
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


# make sure to call the DATABASE the schema you are targeting.


class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #not in the database table
# Now we use class methods to query our database

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        ninja_id= connectToMySQL(DATABASE).query_db(query,data)
        return ninja_id

    @classmethod
    def get_all_ninja(cls):
        query = "SELECT * FROM ninjas;"

    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)

        if not results:
            return[]

        # Create an empty list to append our instances of ninja
        all_ninjas = []
        # Iterate over the db results and create instances of ninja with cls.
        for dict in results:
            all_ninjas.append( cls(dict) )
        return all_ninjas
    @classmethod
    def get_all_ninja_in_dojo(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(id)s;"

    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query, data)

        if not results:
            return[]

        # Create an empty list to append our instances of ninja
        all_ninjas = []
        # Iterate over the db results and create instances of ninja with cls.
        for dict in results:
            all_ninjas.append( cls(dict) )
        return all_ninjas

    @classmethod
    def get_one_ninja(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"

        #datatype = LIST of DICTIONARY
        result = connectToMySQL(DATABASE).query_db(query,data)

        if not result:
            return False
            #return an instance
        return cls( result[0] )

    @classmethod
    def update_one_ninja(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
        
    @classmethod
    def delete_one_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    # Every model should have these methods
    # create / save
    # get_one
    # get_all
    # update_one
    # delete_one