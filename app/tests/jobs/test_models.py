from app.extensions.database import db
from app.jobs.models import Job

def test_job_update(client):
    # updates job's properties
    test_job = Job(
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
    db.session.add(test_job)
    db.session.commit()

    test_job.name = "Doc"
    test_job.save()

    updated_job = Job.query.filter_by(slug="mech").first()
    assert updated_job.name == "Doc"