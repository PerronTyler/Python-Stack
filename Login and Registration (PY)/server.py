from flask_app import app, bcrypt
from flask_app.controllers import controller_user, controller_routes


if __name__=="__main__": 
    app.run(debug=True)