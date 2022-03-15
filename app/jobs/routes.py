from flask import Blueprint, redirect, render_template, url_for

blueprint = Blueprint('jobs', __name__)

jobs = {
    "mechanic": {
        "name": "Mechanic", 
        "salary": "2000", 
        "cashflow": "0",
        "tax": "400", 
        "home_mortgage_payment": "300", 
        "school_loan_payment": "0",
        "car_loan_payment": "100",
        "credit_card_payment": "100",
        "other_expenses": "300",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "700",
        "home_mortgage": "31000",
        "school_loans": "0",
        "car_loans": "3000",
        "credit_card_debt": "3000",
        "payday": "700"
        },
    "janitor": {
        "name": "Janitor", 
        "salary": "1600", 
        "cashflow": "0",
        "tax": "300", 
        "home_mortgage_payment": "200", 
        "school_loan_payment": "0",
        "car_loan_payment": "100",
        "credit_card_payment": "100",
        "other_expenses": "300",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "600",
        "home_mortgage": "20000",
        "school_loans": "0",
        "car_loans": "4000",
        "credit_card_debt": "3000",
        "payday": "600"
        },
    "engineer": {
        "name": "Engineer", 
        "salary": "4900", 
        "cashflow": "0",
        "tax": "1000", 
        "home_mortgage_payment": "700", 
        "school_loan_payment": "100",
        "car_loan_payment": "200",
        "credit_card_payment": "200",
        "other_expenses": "1000",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "400",
        "home_mortgage": "75000",
        "school_loans": "12000",
        "car_loans": "7000",
        "credit_card_debt": "5000",
        "payday": "1700"
        },
    "lawyer": {
        "name": "Lawyer", 
        "salary": "7500", 
        "cashflow": "0",
        "tax": "1800", 
        "home_mortgage_payment": "1100", 
        "school_loan_payment": "300",
        "car_loan_payment": "200",
        "credit_card_payment": "200",
        "other_expenses": "1500",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "2000",
        "home_mortgage": "115000",
        "school_loans": "78000",
        "car_loans": "11000",
        "credit_card_debt": "7000",
        "payday": "2400"
        },
    "officer": {
        "name": "Police Officer", 
        "salary": "3000", 
        "cashflow": "0",
        "tax": "600", 
        "home_mortgage_payment": "400", 
        "school_loan_payment": "0",
        "car_loan_payment": "100",
        "credit_card_payment": "100",
        "other_expenses": "700",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "500",
        "home_mortgage": "46000",
        "school_loans": "0",
        "car_loans": "5000",
        "credit_card_debt": "3000",
        "payday": "1100"
        },
    "pilot": {
        "name": "Airline Pilot", 
        "salary": "9500", 
        "cashflow": "0",
        "tax": "2000", 
        "home_mortgage_payment": "1000", 
        "school_loan_payment": "0",
        "car_loan_payment": "300",
        "credit_card_payment": "700",
        "other_expenses": "2000",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "2500",
        "home_mortgage": "90000",
        "school_loans": "0",
        "car_loans": "15000",
        "credit_card_debt": "22000",
        "payday": "3500"
        },
    "trucker": {
        "name": "Truck Driver", 
        "salary": "2500", 
        "cashflow": "0",
        "tax": "500", 
        "home_mortgage_payment": "400", 
        "school_loan_payment": "0",
        "car_loan_payment": "100",
        "credit_card_payment": "100",
        "other_expenses": "600",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "800",
        "home_mortgage": "38000",
        "school_loans": "0",
        "car_loans": "4000",
        "credit_card_debt": "3000",
        "payday": "800"
        },
    
    "teacher": {
        "name": "Teacher (K-12)", 
        "salary": "3300", 
        "cashflow": "0",
        "tax": "500", 
        "home_mortgage_payment": "500", 
        "school_loan_payment": "100",
        "car_loan_payment": "100",
        "credit_card_payment": "200",
        "other_expenses": "700",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "400",
        "home_mortgage": "50000",
        "school_loans": "12000",
        "car_loans": "5000",
        "credit_card_debt": "4000",
        "payday": "1200"
        },
    "manager": {
        "name": "Business Manager", 
        "salary": "4600", 
        "cashflow": "0",
        "tax": "900", 
        "home_mortgage_payment": "700", 
        "school_loan_payment": "100",
        "car_loan_payment": "100",
        "credit_card_payment": "200",
        "other_expenses": "1000",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "400",
        "home_mortgage": "75000",
        "school_loans": "12000",
        "car_loans": "6000",
        "credit_card_debt": "4000",
        "payday": "1600"
        },
    "doc": {
        "name": "Doctor", 
        "salary": "13200", 
        "cashflow": "0",
        "tax": "3200", 
        "home_mortgage_payment": "1900", 
        "school_loan_payment": "700",
        "car_loan_payment": "300",
        "credit_card_payment": "200",
        "other_expenses": "2000",
        "bank_loan_payment": "0",
        "children": "0",
        "savings": "3500",
        "home_mortgage": "202000",
        "school_loans": "150000",
        "car_loans": "19000",
        "credit_card_debt": "10000",
        "payday": "4900"
        }
}

@blueprint.route('/jobs')
def choose_job():
    #Log:
    print('CHOOSE YOUR JOB')

    return render_template("jobs/choose_job.html", jobs=jobs)

@blueprint.route('/play')
def play():
    # Log:
    print('REDIRECT /play TO /jobs')

    return redirect(url_for('jobs.choose_job'))

@blueprint.route('/jobs/<slug>')
def job_dynamic(slug):
    # Log:
    print(F'CHOSE {jobs[slug]["name"].upper()} AS JOB, HERE ARE YOUR STATS')

    return render_template("jobs/job_dynamic.html", job=slug, jobs=jobs)