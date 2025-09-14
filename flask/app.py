"""
To run:
1. cd flask
2. flask run OR python -m flask run
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Create your data structure(s) here:

# Complete the API endpoints below:

@app.route('/movies', methods=['POST'])
def add_movie():
    return 200, jsonify({})

@app.route('/movies', methods=['GET'])
def get_movies():
    return 200, jsonify({})

@app.route('/movies', methods=['GET'])
def search_by_title():
    return 200, jsonify({})

@app.route('/movies/<movie_id>/rating', methods=['PUT'])
def update_rating(movie_id):
    return 200, jsonify({})