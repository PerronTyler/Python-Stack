from flask import Flask
DATABASE = 'users_schema'
app = Flask(__name__)
app.secret_key = "10a34980-7359-4624-82e9-cc4f8b9ab963"
