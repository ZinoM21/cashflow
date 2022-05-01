from app.extensions.database import db
from app.users.models import User
from werkzeug.security import generate_password_hash

def test_user_update(client):
    # updates user's properties

    # Arrange
    test_user = User(
        email = "test@code.berlin",
        password =generate_password_hash('12345678'),
        uname = 'tester',
        fname = 'testfname',
        lname = 'testlname'
        )
    db.session.add(test_user)
    db.session.commit()

    # Act
    test_user.fname = "Markus"
    test_user.save()

    # Assert
    updated_user = User.query.filter_by(email="test@code.berlin").first()
    assert updated_user.fname == "Markus"

def test_user_delete(client):
    # deletes user

    # Arrange
    test_user = User(
        email = "test@code.berlin",
        password =generate_password_hash('12345678'),
        uname = 'tester',
        fname = 'testfname',
        lname = 'testlname'
        )
    db.session.add(test_user)
    db.session.commit()

    # Act
    test_user.delete()

    # Assert
    deleted_user = User.query.filter_by(email="test@code.berlin").first()
    assert deleted_user is None