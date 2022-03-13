from doctest import ELLIPSIS_MARKER
from flask import Flask, redirect, url_for, render_template, send_file
from random import randint

app = Flask(__name__)
app.config.from_object('app.config')

jobs = {
    "mechanic": {
        "name": "Mechanic", 
        "income": "2000", 
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
        "credit_card_debt": "3000"
        },
    "janitor": {
        "name": "Janitor", 
        "income": "1600", 
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
        "credit_card_debt": "3000"
        },
    "engineer": {
        "name": "Engineer", 
        "income": "4900", 
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
        },
    "lawyer": {
        "name": "Lawyer", 
        "income": "7500", 
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
        },
    "officer": {
        "name": "Police Officer", 
        "income": "3000", 
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
        },
    "pilot": {
        "name": "Airline Pilot", 
        "income": "9500", 
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
        "credit_card_debt": "22000"
        },
    "trucker": {
        "name": "Truck Driver", 
        "income": "2500", 
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
        "credit_card_debt": "3000"
        },
    
    "teacher": {
        "name": "Teacher (K-12)", 
        "income": "3300", 
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
        },
    "manager": {
        "name": "Business Manager", 
        "income": "4600", 
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
        "credit_card_debt": "4000"
        },
    "doc": {
        "name": "Doctor", 
        "income": "13200", 
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
        "credit_card_debt": "10000"
        }
}

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/playing')
def playing():
    return render_template("playing.html", jobs=jobs)

@app.route('/playing/<slug>')
def playing_job(slug):
    return render_template("playing_job.html", job=slug, jobs=jobs)

@app.route('/login')
def login():
    return render_template("login.html")