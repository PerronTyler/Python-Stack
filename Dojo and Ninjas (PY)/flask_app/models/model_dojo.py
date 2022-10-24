# import the function that will return an instance of a connection
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


# make sure to call the DATABASE the schema you are targeting.


class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #not in the database table
# Now we use class methods to query our database

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo_id= connectToMySQL(DATABASE).query_db(query,data)
        return dojo_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)

        if not results:
            return[]

        # Create an empty list to append our instances of dojo
        all_dojos = []
        # Iterate over the db results and create instances of dojo with cls.
        for dict in results:
            all_dojos.append( cls(dict) )
        return all_dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"

        #datatype = LIST of DICTIONARY
        result = connectToMySQL(DATABASE).query_db(query,data)

        if not result:
            return False
            #return an instance
        return cls( result[0] )

    @classmethod
    def update_one(cls, data):
        query = "UPDATE dojos SET name=%(name)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
        
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    # Every model should have these methods
    # create / save
    # get_one
    # get_all
    # update_one
    # delete_one