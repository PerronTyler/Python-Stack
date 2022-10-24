## pre-requirements
 - install pipenv `globally`
 ```
 pip install pipenv
 ```

 # Flask Checklist
 - create a directory 
 - go into that folder
 - create virtual env
  ```
  pipenv install flask pymysql flask-bcrypt
  ```
  - `WARNING!` look for the files __pipfile__ && __pipfile.lock__
    - if you do not see these you need to figure it out right away
- Activate it / go into the "world" aka: the shell
```
 pipenv shell
```
```
 - set up the file structure

     - Main app folder
        -flask_app
            -config
                -mysqlconnection.py
            -controllers
                -controller_tablename.py
                -controller_routes.py
            -models
                -model_table_name.py
            -Static
                -css
                    -style.css
                -js
                    -script.js
            -Templates
                -index.html
                -template.html
            -__init__.py
       - pipfile
       - pipfile.lock
       - server.py
```

- input boilerplate code into files
- test to make sure your application works!
  ```
  python server.py
  ```

- should be running on the port 127.0.0.1:5000 or localhost:5000

    ## server.py
```py
from flask_app import app
from flask_app.controllers import controller_tablename, controller_routes

if __name__=="__main__":       
    app.run(debug=True)
```
## mysqlconnection.py
```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

## model.py
```py
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session

# make sure to call the DATABASE the schema you are targeting.
DATABASE = 'tablename_db'

class Tablename:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #not in the database table
        self.fullname = f"{self.first_name} {self.last_name}"
    # Now we use class methods to query our database

    @classmethod
    def create(cls, data):
      query = "INSERT INTO tablename (columname1. columname2) VALUES (%(columname1)s, %(columname2)s);"
      tablename_id= MySQLConnection(DATABASE).query_db(query,data)
      return tablename_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tablename;"

        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)

        if not results:
            return[]

        # Create an empty list to append our instances of tablename
        all_tablename = []
        # Iterate over the db results and create instances of tablename with cls.
        for dict in results:
            all_tablename.append( cls(dict) )
        return all_tablename

    @classmethod
    def get_one(cls,data):
      query = "SELECT * FROM tablename WHERE id = %(id)s"
      
      #datatype = LIST of DICTIONARY
      result = connectToMySQL(DATABASE).query_db(query,data)

      if not result:
        return False
      #return an instance
      return cls( result[0] )

    @classmethod
    def update_one(cls, data):
      query = "UPDATE tablename SET columname1=%(columname1)s, columname2=%(columname2)s WHERE id=%(id)s;"
      return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_one(cls):
      pass

      # Every model should have these methods
      # create / save
      # get_one
      # get_all
      # update_one
      # delete_one
```
## Controller file
```py
from flask import render_template, redirect, request, session 
from flask_app import app, bcrypt

from flask_app.models.model_tablename import Tablename
# from flask_app.config.helper import findBool IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST


@app.route('/tablename/new')
def tablename_new():
    return render_template('tablename_new.html')

    # Action route
@app.route('/tablename/create', methods=['POST'])
def tablename_create():
    data = {
        **request.form
    }
    # data = findBool(data, 'Boolean Key Name') IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST
    Tablename.update_one(data)

    return redirect('/')

@app.route('/tablename/<int:id>')
def tablename_show(id):

    return render_template('burger_show.html')

@app.route('/tablename/<int:id>/edit')
def tablename_edit(id):
    tablename = Tablename.get_one({'id':id})

    return render_template('tablename_edit.html', tablename=tablename)

@app.route('/tablename/<int:id>/update', methods=['POST'])
def tablename_update(id):
    data = {
        **request.form
        'id':id
    }
    # data = findBool(data, 'Boolean Key Name') IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST

    Tablename.update_one(data)
    return redirect('/')

@app.route('/tablename/<int:id>/delete')
def tablename_delete(id):
    Tablename.delete_one({'id': id})

    return redirect('/')
```

## Controller_Routes.py
```py
from flask import render_template, redirect, request, session 
from flask_app import app, bcrypt

from flask_app.models.model_tablename import Tablename

@app.route('/')          
def hello_world():
    return render_template('index.html')  
```

## __init__.py
```py
from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "10a34980-7359-4624-82e9-cc4f8b9ab963"

bcrypt = Bcrypt(app)
```