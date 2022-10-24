from flask import render_template, redirect, request, session 
from flask_app import app

from flask_app.models.model_survey import Survey

@app.route('/')          
def hello_world():
    session.clear()
    return render_template('index.html')  