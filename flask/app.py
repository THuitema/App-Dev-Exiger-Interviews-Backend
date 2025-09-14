"""
To run:
1. cd flask
2. flask run OR python -m flask run
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello, World!</p>'