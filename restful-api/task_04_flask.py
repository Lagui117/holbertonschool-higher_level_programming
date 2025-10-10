#!/usr/bin/env python3
"""
Task 04 - Simple API using Flask.

Routes:
  GET  /                 -> "Welcome to the Flask API!"
  GET  /status           -> "OK"
  GET  /data             -> JSON list of usernames
  GET  /users/<username> -> JSON user or {"error": "User not found"}
  POST /add_user         -> add user via JSON body
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store (empty by default for the checker)
users = {}
# Example (do not pre-seed when submitting):
# users["jane"] = {"username": "jane", "name": "Jane", "age": 28, "city": "LA"}


@app.get("/")
def home():
    return "Welcome to the Flask API!"


@app.get("/status")
def status():
    return "OK"


@app.get("/data")
def data():
    """Return the list of usernames (keys of users)."""
    return jsonify(list(users.keys()))


@app.get("/users/<username>")
def get_user(username: str):
    """Return the full user object or a standard error body."""
    user = users.get(username)
    if not user:
        err = {"error": "User not found"}
        return jsonify(err), 200
    return jsonify(user)


@app.post("/add_user")
def add_user():
    """Add a user from JSON payload."""
    if not request.is_json:
        return jsonify({"error": "Expected application/json"}), 400

    payload = request.get_json(silent=True) or {}
    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    user = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }
    users[username] = user
    body = {"message": "User added", "user": user}
    return jsonify(body), 201


if __name__ == "__main__":
    # Recommended: flask --app task_04_flask.py run
    app.run(host="0.0.0.0", port=5000)
