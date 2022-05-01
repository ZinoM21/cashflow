from app.users.models import User
from werkzeug.security import generate_password_hash
from flask_login import login_user


### SIGNUP ###
def test_signup_success(client):
    # Page loads
    response = client.get('/signup')
    assert response.status_code == 200

def test_signup_content(client):
    # Returns login text
    response = client.get('/signup')
    assert b'Already have an account?' in response.data

def test_post_signup(client):
    # Creates a user record

    # Arrange
    response = client.post('/signup', data={
        'username': 'johndoe',
        'password': '12345678',
        'password_confirmation': '12345678'

    })
    
    # Assert
    assert response.status_code == 302


### LOGIN ###
def test_login_success(client):
    # Page loads
    response = client.get('/login')
    assert response.status_code == 200

def test_login_content(client):
    # Returns login text
    response = client.get('/login')
    assert b'You can log in to save and look up your recent gameplays' in response.data
    
def test_post_login(client):
    # test if login possible & redirect

    # Arrange
    user = User(
        email = 'test@code.berlin',
        password = generate_password_hash('12345678')
    )
    user.save()

    # Act
    response = client.post('/login', data={
        'email': 'test@code.berlin',
        'password': '12345678'
    })

    # Assert
    assert response.status_code == 302


### LOGOUT ####
def test_logout_success(client):
    # Page loads

    # Act
    response = client.get('/logout')

    # Assert
    assert response.status_code == 302


### ACCOUNT ###
def test_login_success(client):
    # Page loads
    response = client.get('/login')
    assert response.status_code == 200

def test_login_content(client):
    # Returns login text
    response = client.get('/login')
    assert b'You can log in to save and look up your recent gameplays' in response.data
    
def test_post_login(client):
    # test if login possible & redirect

    # Arrange
    user = User(
        email = 'test@code.berlin',
        password = generate_password_hash('12345678')
    )
    user.save()

    # Act
    response = client.post('/login', data={
        'email': 'test@code.berlin',
        'password': '12345678'
    })

    # Assert
    assert response.status_code == 302

