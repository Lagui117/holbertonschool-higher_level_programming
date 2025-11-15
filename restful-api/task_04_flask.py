#!/usr/bin/python3
"""
Task 04 - Simple API using Flask.

Endpoints:
  GET  /               -> Welcome message
  GET  /data           -> List of all usernames
  GET  /status         -> "OK"
  GET  /users/<username> -> User object or 404
  POST /add_user       -> Add new user, return 201 or error
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users stored in memory (dictionary with username as key)
users = {}


@app.route('/')
def home():
    """Welcome endpoint."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Return OK status."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user object or 404 if not found."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user.

    Expected JSON body:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    Returns:
        201: User added successfully
        400: Invalid JSON or missing username
        409: Username already exists
    """
    # Check if request body is valid JSON
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # If get_json() returns None, it's not valid JSON
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if username is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to dictionary
    users[username] = data

    # Return success message with user data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()