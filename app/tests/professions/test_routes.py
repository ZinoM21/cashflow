from app.extensions.database import db
from app.professions.models import Profession

### ------ TEST PROFESSIONS PAGINATED ------- ###

def test_professions_success(client):
    # Page loads
    response = client.get('/professions')
    assert response.status_code == 200

def test_jobs_redirect(client):
    # Page redirects to /professions
    response = client.get('/jobs')
    assert response.status_code == 302


### ------- TEST SINGLE PROFESSION VIEW ------- ###

def test_profession_dynamic_success(client):
    # Page loads

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
    response = client.get('/professions/' + test_profession.slug)

    # Assert
    assert response.status_code == 200

def test_job_dynamic_redirect(client):
    # Page redirects to /professions
    
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
    response = client.get('/jobs/' + test_profession.slug)

    # Assert
    assert response.status_code == 302
