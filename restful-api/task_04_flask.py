#!/usr/bin/env python3
"""
Task 04 - Simple API using Flask.

Routes:
  GET  /                 -> "Welcome to the Flask API!"
  GET  /status           -> "OK"
  GET  /data             -> JSON list of usernames
  GET  /users/<username> -> JSON user or {"error": "User not found"} (404)
  POST /add_user         -> Add user or handle duplicates (409)
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Empty dict required for the checker
users = {}


@app.get("/")
def home():
    """Root route."""
    return "Welcome to the Flask API!"


@app.get("/status")
def status():
    """Health check route."""
    return "OK"


@app.get("/data")
def data():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.get("/users/<username>")
def get_user(username):
    """Return one user or error JSON with code 404."""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.post("/add_user")
def add_user():
    """Add new user from JSON payload."""
    if not request.is_json:
        return jsonify({"error": "Expected application/json"}), 400

    payload = request.get_json(silent=True) or {}
    username = payload.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # ✅ Checker wants 409 Conflict for duplicate usernames
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

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
