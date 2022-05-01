def test_api_professions_success(client):
    # Data loads

    # Act
    response = client.get('/api/v1/professions')

    # Assert
    assert response.status_code == 200

def test_api_professions_content(client):
    # Returns json array

    # Act
    response = client.get('/api/v1/professions')

    # Assert
    assert b'[]' in response.data
