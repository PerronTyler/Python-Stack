# import the function that will return an instance of a connection
from flask import flash, session

# make sure to call the DATABASE the schema you are targeting.
# DATABASE = 'tablename_db'

class Survey:
    def __init__( self , data ):
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

#         #not in the database table
# # Now we use class methods to query our database

#     @classmethod
#     def create(cls, data):
#         query = "INSERT INTO tablename (columname1. columname2) VALUES (%(columname1)s, %(columname2)s);"
#         tablename_id= MySQLConnection(DATABASE).query_db(query,data)
#         return tablename_id

# @classmethod
# def get_all(cls):
#     query = "SELECT * FROM tablename;"

# # make sure to call the connectToMySQL function with the schema you are targeting.
#     results = connectToMySQL(DATABASE).query_db(query)

#     if not results:
#         return[]

#     # Create an empty list to append our instances of tablename
#     all_tablename = []
#     # Iterate over the db results and create instances of tablename with cls.
#     for dict in results:
#         all_tablename.append( cls(dict) )
#     return all_tablename

# @classmethod
# def get_one(cls,data):
#     query = "SELECT * FROM tablename WHERE id = %(id)s"

#     #datatype = LIST of DICTIONARY
#     result = connectToMySQL(DATABASE).query_db(query,data)

#     if not result:
#         return False
#         #return an instance
#     return cls( result[0] )

# @classmethod
# def update_one(cls, data):
#     query = "UPDATE tablename SET columname1=%(columname1)s, columname2=%(columname2)s WHERE id=%(id)s;"
#     return connectToMySQL(DATABASE).query_db(query,data)
    
# @classmethod
# def delete_one(cls):
#     pass

# # Every model should have these methods
# # create / save
# # get_one
# # get_all
# # update_one
# # delete_one