from app.extensions.database import db
from app.professions.models import Profession

# A user is not allowed to create, update or delete data from this table, but I found it good to test and practice tests here

def test_profession_update(client):
    # updates profession's properties

    # Arrange
    test_profession = Profession(
        slug="mech",
        name="Mech", 
        salary=123, 
        cashflow=234, 
        tax=345, 
        home_mortgage_payment=456, 
        school_loan_payment=567, 
        car_loan_payment=678, 
        credit_card_payment=789, 
        other_expenses=890, 
        bank_loan_payment=1235, 
        children=1,
        children_expenses=8765,
        savings=3467, 
        home_mortgage=34543543, 
        school_loans=4737, 
        car_loans=546345, 
        credit_card_debt=76365, 
        payday=675675
        )
    db.session.add(test_profession)
    db.session.commit()

    # Act
    test_profession.name = "Doc"
    test_profession.save()

    # Assert
    updated_profession = Profession.query.filter_by(slug="mech").first()
    assert updated_profession.name == "Doc"

def test_profession_delete(client):
    # deletes profession

    # Arrange
    test_profession = Profession(
        slug="mech",
        name="Mech", 
        salary=123, 
        cashflow=234, 
        tax=345, 
        home_mortgage_payment=456, 
        school_loan_payment=567, 
        car_loan_payment=678, 
        credit_card_payment=789, 
        other_expenses=890, 
        bank_loan_payment=1235, 
        children=4236,
        savings=3467, 
        home_mortgage=34543543, 
        school_loans=4737, 
        car_loans=546345, 
        credit_card_debt=76365, 
        payday=675675
        )
    db.session.add(test_profession)
    db.session.commit()

    # Act
    test_profession.delete()

    # Assert
    deleted_profession = Profession.query.filter_by(slug="mech").first()
    assert deleted_profession is None