#!/usr/bin/env python3
"""
Task 04 - Simple API using Flask.

Routes:
  GET  /                 -> "Welcome to the Flask API!"
  GET  /status           -> "OK"
  GET  /data             -> JSON list of usernames
  GET  /users/<username> -> JSON user or {"error": "User not found"} (404)
  POST /add_user         -> add user via JSON body
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store (empty for checker)
users = {}


@app.get("/")
def home():
    return "Welcome to the Flask API!"


@app.get("/status")
def status():
    return "OK"


@app.get("/data")
def data():
    """Return the list of usernames."""
    return jsonify(list(users.keys()))


@app.get("/users/<username>")
def get_user(username):
    """Return a user object or a JSON error with 404."""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.post("/add_user")
def add_user():
    """Add a user to the in-memory database."""
    if not request.is_json:
        return jsonify({"error": "Expected application/json"}), 400

    payload = request.get_json(silent=True) or {}
    username = payload.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    user = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }

    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
