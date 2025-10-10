#!/usr/bin/env python3
"""
Task 05 - API Security and Authentication Techniques with Flask.

Includes:
- Basic HTTP Auth (Flask-HTTPAuth)
- JWT Auth (Flask-JWT-Extended)
- Role-based access control (admin-only)

All authentication errors must return HTTP 401.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-me-super-secret"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users; passwords are hashed
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_basic_auth(username, password):
    """Verify Basic Auth credentials."""
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user["username"]
    return None


@app.get("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic-auth protected resource."""
    return "Basic Auth: Access Granted"


@app.post("/login")
def login():
    """Issue a JWT if credentials are valid."""
    if not request.is_json:
        return jsonify({"error": "Missing JSON"}), 401

    payload = request.get_json(silent=True) or {}
    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    identity = {"username": username, "role": user["role"]}
    token = create_access_token(identity=identity)
    return jsonify({"access_token": token})


@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT-protected route."""
    return "JWT Auth: Access Granted"


@app.get("/admin-only")
@jwt_required()
def admin_only():
    """Admin-only route, requires role 'admin'."""
    ident = get_jwt_identity()
    role = (ident or {}).get("role")
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """No/invalid Authorization header (Bearer)."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Token cannot be decoded/verified."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Token is expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Token has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Fresh token required but not provided."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    # Recommended: flask --app task_05_basic_security.py run --port 5001
    app.run(host="0.0.0.0", port=5001)
