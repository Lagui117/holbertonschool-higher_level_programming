import pytest
import base64
from task_05_basic_security import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_basic_protected_without_credentials(client):
    response = client.get('/basic-protected')
    assert response.status_code == 401

def test_basic_protected_with_valid_credentials(client):
    credentials = base64.b64encode(b'user1:password').decode('utf-8')
    response = client.get('/basic-protected', headers={'Authorization': f'Basic {credentials}'})
    assert response.status_code == 200
    assert response.data == b"Basic Auth: Access Granted"

def test_login_with_valid_credentials(client):
    response = client.post('/login', json={'username': 'user1', 'password': 'password'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_jwt_protected_without_token(client):
    response = client.get('/jwt-protected')
    assert response.status_code == 401

def test_jwt_protected_with_valid_token(client):
    login_response = client.post('/login', json={'username': 'user1', 'password': 'password'})
    token = login_response.json['access_token']
    response = client.get('/jwt-protected', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.data == b"JWT Auth: Access Granted"

def test_admin_only_with_non_admin_token(client):
    login_response = client.post('/login', json={'username': 'user1', 'password': 'password'})
    token = login_response.json['access_token']
    response = client.get('/admin-only', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 403
    assert response.json == {"error": "Admin access required"}

def test_admin_only_with_admin_token(client):
    login_response = client.post('/login', json={'username': 'admin1', 'password': 'password'})
    token = login_response.json['access_token']
    response = client.get('/admin-only', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.data == b"Admin Access: Granted"