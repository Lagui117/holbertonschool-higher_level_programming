#!/usr/bin/env python3
"""
Task 05 - API Security with Flask.
- Basic Auth (custom, sans Flask-HTTPAuth)
- JWT (Flask-JWT-Extended)
- RBAC: /admin-only pour role 'admin'
Toutes les erreurs JWT => 401 JSON {"error": "..."}.
"""
from flask import Flask, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
import base64

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-me-super-secret"
jwt = JWTManager(app)

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


def _parse_basic_auth(auth_header: str):
    if not auth_header or not auth_header.startswith("Basic "):
        return None, None
    try:
        b64 = auth_header.split(" ", 1)[1]
        decoded = base64.b64decode(b64).decode("utf-8")
        username, password = decoded.split(":", 1)
        return username, password
    except Exception:
        return None, None


def _require_basic_auth():
    username, password = _parse_basic_auth(request.headers.get("Authorization"))
    if not username or not password:
        resp = make_response(jsonify({"error": "Missing credentials"}), 401)
        resp.headers["WWW-Authenticate"] = 'Basic realm="Login Required"'
        return resp

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        resp = make_response(jsonify({"error": "Invalid credentials"}), 401)
        resp.headers["WWW-Authenticate"] = 'Basic realm="Login Required"'
        return resp
    return None


@app.get("/basic-protected")
def basic_protected():
    failed = _require_basic_auth()
    if failed is not None:
        return failed
    return "Basic Auth: Access Granted"


@app.post("/login")
def login():
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
    return "JWT Auth: Access Granted"


@app.get("/admin-only")
@jwt_required()
def admin_only():
    ident = get_jwt_identity() or {}
    if ident.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err_msg):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err_msg):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
