def test_root_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200

def test_home_redirect(client):
    # Page redirects to root
    response = client.get('/home')
    assert response.status_code == 302

def test_login_success(client):
    # Page loads
    response = client.get('/login')
    assert response.status_code == 200