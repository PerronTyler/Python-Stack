from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

from flask_app import app
from flask_app.controllers import controller_tablename