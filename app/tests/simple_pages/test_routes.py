
### ROOT ###

def test_root_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200

def test_root_content(client):
    # Returns 'are you sick' text
    response = client.get('/')
    assert b'Are you sick of recalculating your cashflow round by round' in response.data

def test_home_redirect(client):
    # Page redirects to root
    response = client.get('/home')
    assert response.status_code == 302

def test_start_redirect(client):
    # Page redirects to root
    response = client.get('/start')
    assert response.status_code == 302


### FAQ ###

def test_faq_success(client):
    # Page loads
    response = client.get('/faq')
    assert response.status_code == 200

def test_faq_content(client):
    # Returns 'click here' text
    response = client.get('/faq')
    assert b'Click here to find all rules' in response.data


### IMPRINT ###

def test_imprint_success(client):
    # Page loads
    response = client.get('/imprint')
    assert response.status_code == 200

def test_imprint_content(client):
    # Returns 'imprint' text
    response = client.get('/imprint')
    assert b'Imprint' in response.data


### PRIVACY ###

def test_imprint_success(client):
    # Page loads
    response = client.get('/privacy')
    assert response.status_code == 200

def test_imprint_content(client):
    # Returns 'privacy' text
    response = client.get('/privacy')
    assert b'Privacy' in response.data