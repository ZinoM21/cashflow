from app.simple_pages.models import User

def test_root_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200

def test_root_content(client):
    # Returns are you sick text
    response = client.get('/')
    assert b'Are you sick of recalculating your cashflow round by round' in response.data

def test_home_redirect(client):
    # Page redirects to root
    response = client.get('/home')
    assert response.status_code == 302

def test_login_success(client):
    # Page loads
    response = client.get('/login')
    assert response.status_code == 200

def test_login_content(client):
    # Returns login text
    response = client.get('/login')
    assert b'You can log in to save and look up your recent gameplays' in response.data

def test_post_signup_creates_user(client):
    # Creates a user record
    response = client.post('/signup', data={
        'username': 'johndoe',
        'password': '12345678'
    })
    assert User.query.first() is not None