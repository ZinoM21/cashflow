def test_choose_profession_success(client):
    # Page loads
    response = client.get('/professions')
    assert response.status_code == 200

def test_play_redirect(client):
    # Page redirects to /professions
    response = client.get('/play')
    assert response.status_code == 302
