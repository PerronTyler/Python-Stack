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
  from flask import Flask, render_template  # Import Flask to allow us to create our app
  app = Flask(__name__) 
     # Create a new instance of the Flask class called "app"
  @app.route('/')          # The "@" decorator associates this route with the function immediately following
  def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response
  if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


```