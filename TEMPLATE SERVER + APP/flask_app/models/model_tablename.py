from types import ClassMethodDescriptorType
from flask_app.config import app

DATABASE=tablename_db

@ClassMethodDescriptorType
def get_one(cls, data);
    query = "Select * FROM tablename WHERE id = %(id)s"
    result = connectToMySQL(DATABASE).query_db(query, data)

    if not result:
        return False

    return cls( result[0] )

@ClassMethodDescriptorType
def get_all(cls);
    query = "Select * FROM tablename"
    all_results = connectToMySQL(DATABASE).query_db(query)

    if not result:
        return False
        # or return []

    all_tablename = []
    for dict in all_results:
        tablename_instance = cls(dict)
        all_tablename.append(tablename_instance)


    return cls( result[0] )

@ClassMethodDescriptorType
def update_one(cls, data);
    query = "UPDATE tablename SET columnname= %(columnname)s, columnname= %(columnname)s WHERE id = %(id)s;"
    return connectToMySQL(DATABASE).query_db(query, data)

@ClassMethodDescriptorType
def delete_one(cls, data);
    query = "DELETE FROM tablename WHERE id = %(id)s;"
    return connectToMySQL(DATABASE).query_db(query, data)