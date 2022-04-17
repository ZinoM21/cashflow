from app.extensions.database import db
from app.professions.models import Profession

def test_profession_update(client):
    # updates profession's properties
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

    test_profession.name = "Doc"
    test_profession.save()

    updated_profession = Profession.query.filter_by(slug="mech").first()
    assert updated_profession.name == "Doc"

def test_profession_delete(client):
    # deletes profession
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

    test_profession.delete()

    deleted_profession = Profession.query.filter_by(slug="mech").first()
    assert deleted_profession is None