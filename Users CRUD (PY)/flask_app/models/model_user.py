# import the function that will return an instance of a connection
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


# make sure to call the DATABASE the schema you are targeting.


class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #not in the database table
# Now we use class methods to query our database

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email ) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        user_id= connectToMySQL(DATABASE).query_db(query,data)
        return user_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)

        if not results:
            return[]

        # Create an empty list to append our instances of user
        all_users = []
        # Iterate over the db results and create instances of user with cls.
        for dict in results:
            all_users.append( cls(dict) )
        return all_users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"

        #datatype = LIST of DICTIONARY
        result = connectToMySQL(DATABASE).query_db(query,data)

        if not result:
            return False
            #return an instance
        return cls( result[0] )

    @classmethod
    def update_one(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
        
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    # Every model should have these methods
    # create / save
    # get_one
    # get_all
    # update_one
    # delete_one