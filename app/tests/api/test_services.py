# @blueprint.get('/api/v1/professions')
# def professions():
#     professions = Profession.query.all()

#     return jsonify(
#         serialize_professions(professions)
#     )

from cgi import test
from app.api.services.serialize_professions import serialize_professions
from app.professions.models import Profession

def test_serialize_professions(client):
    # test if serialize_professions funtions works

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
    test_profession.save()
    test_professions = Profession.query.all()

    # Act
    test_list = serialize_professions(test_professions)

    # Assert
    assert test_list[0]['Taxes'] == 345