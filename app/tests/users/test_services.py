from app.users.services.create_user import create_user
from app.users.services.change_user import change_user


def test_create_user(client):
    # test user creation function

    # Arrange
    form_data={
        "email": "test@code.berlin",
        "password": "12345678"
    }

    # Act
    user = create_user(form_data)

    # Assert
    assert user.email == "test@code.berlin"


def test_change_user(client):
    # test user changing function

    # Arrange
    initial_data = {
        "email": "initial@code.berlin",
        "password": "12345678"
    }

    user = create_user(initial_data)

    form_data = {
        "email": "new@code.berlin"
    }

    # Act
    updated_user = change_user(form_data, user)

    # Assert
    assert updated_user.email == "new@code.berlin"