from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "10a34980-7359-4624-82e9-cc4f8b9ab963"

DATABASE = 'login_registration_schema'

bcrypt = Bcrypt(app)