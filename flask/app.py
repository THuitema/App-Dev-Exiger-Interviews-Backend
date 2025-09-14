"""
To run:
1. cd flask
2. flask run OR python -m flask run
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/movies')
def add_movie():
    return 200, jsonify({})

@app.route('/movies')
def get_movies():
    return 200, jsonify({})

@app.route('/movies')
def search_by_title():
    return 200, jsonify({})

@app.route('/movies/<movie_id>/rating')
def update_rating(movie_id):
    return 200, jsonify({})