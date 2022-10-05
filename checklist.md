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
  pipenv install flask
  ```
  - `WARNING!` look for the files __pipfile__ && __pipfile.lock__
    - if you do not see these you need to figure it out right away
- Activate it / go into the "world" aka: the shell
```
 pipenv shell
```
 - set up the file structure
    ```
     - Main app folder
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
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/')          
def hello_world():
    return render_template('index.html')  
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
     
                cursor.execute(query)
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
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
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
    def create(cls):
      pass

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        all_friends = []
        # Iterate over the db results and create instances of friends with cls.
        for dict in results:
            all_friends.append( cls(dict) )
        return all_friends

    @classmethod
    def get_one(cls):
      pass
    

    @classmethod
    def update_one(cls):
      pass
    
    
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
