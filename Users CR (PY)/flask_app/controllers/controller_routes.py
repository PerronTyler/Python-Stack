from flask import render_template, redirect, request, session 
from flask_app import app

from flask_app.models.model_user import User

@app.route('/')          
def hello_world():
    return render_template('index.html')  