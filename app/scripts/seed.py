from app.app import create_app
from app.professions.models import Profession
from app.opportunities.models import Opportunity
from app.extensions.database import db

app = create_app()
app.app_context().push()


# Professions

all_professions_dict = {
    "mechanic": {
        "Name": "Mechanic", 
        "Salary": 2000, 
        "Cashflow": 0,
        "Taxes": 400, 
        "Home Mortgage Payment": 300, 
        "School Loan Payment": 0,
        "Car Loan Payment": 100,
        "Credit Card Payment": 100,
        "Other Expenses": 400,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 700,
        "Home Mortgage": 31000,
        "School Loans": 0,
        "Car Loans": 3000,
        "Credit Card Debt": 3000,
        "PayDay": 700
        },
    "janitor": {
        "Name": "Janitor", 
        "Salary": 1600, 
        "Cashflow": 0,
        "Taxes": 300, 
        "Home Mortgage Payment": 200, 
        "School Loan Payment": 0,
        "Car Loan Payment": 100,
        "Credit Card Payment": 100,
        "Other Expenses": 300,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 600,
        "Home Mortgage": 20000,
        "School Loans": 0,
        "Car Loans": 4000,
        "Credit Card Debt": 3000,
        "PayDay": 600   
        },
    "engineer": {
        "Name": "Engineer", 
        "Salary": 4900, 
        "Cashflow": 0,
        "Taxes": 1000, 
        "Home Mortgage Payment": 700, 
        "School Loan Payment": 100,
        "Car Loan Payment": 200,
        "Credit Card Payment": 200,
        "Other Expenses": 1000,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 400,
        "Home Mortgage": 75000,
        "School Loans": 12000,
        "Car Loans": 7000,
        "Credit Card Debt": 5000,
        "PayDay": 1700
        },
    "lawyer": {
        "Name": "Lawyer", 
        "Salary": 7500, 
        "Cashflow": 0,
        "Taxes": 1800, 
        "Home Mortgage Payment": 1100, 
        "School Loan Payment": 300,
        "Car Loan Payment": 200,
        "Credit Card Payment": 200,
        "Other Expenses": 1500,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 2000,
        "Home Mortgage": 115000,
        "School Loans": 78000,
        "Car Loans": 11000,
        "Credit Card Debt": 7000,
        "PayDay": 2400
        },
    "officer": {
        "Name": "Police Officer", 
        "Salary": 3000, 
        "Cashflow": 0,
        "Taxes": 600, 
        "Home Mortgage Payment": 400, 
        "School Loan Payment": 0,
        "Car Loan Payment": 100,
        "Credit Card Payment": 100,
        "Other Expenses": 700,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 500,
        "Home Mortgage": 46000,
        "School Loans": 0,
        "Car Loans": 5000,
        "Credit Card Debt": 3000,
        "PayDay": 1100
        },
    "pilot": {
        "Name": "Airline Pilot", 
        "Salary": 9500, 
        "Cashflow": 0,
        "Taxes": 2000, 
        "Home Mortgage Payment": 1000, 
        "School Loan Payment": 0,
        "Car Loan Payment": 300,
        "Credit Card Payment": 700,
        "Other Expenses": 2000,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 2500,
        "Home Mortgage": 90000,
        "School Loans": 0,
        "Car Loans": 15000,
        "Credit Card Debt": 22000,
        "PayDay": 3500
        },
    "trucker": {
        "Name": "Truck Driver", 
        "Salary": 2500, 
        "Cashflow": 0,
        "Taxes": 500, 
        "Home Mortgage Payment": 400, 
        "School Loan Payment": 0,
        "Car Loan Payment": 100,
        "Credit Card Payment": 100,
        "Other Expenses": 600,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 800,
        "Home Mortgage": 38000,
        "School Loans": 0,
        "Car Loans": 4000,
        "Credit Card Debt": 3000,
        "PayDay": 800
        },
    
    "teacher": {
        "Name": "Teacher (K-12)", 
        "Salary": 3300, 
        "Cashflow": 0,
        "Taxes": 500, 
        "Home Mortgage Payment": 500, 
        "School Loan Payment": 100,
        "Car Loan Payment": 100,
        "Credit Card Payment": 200,
        "Other Expenses": 700,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 400,
        "Home Mortgage": 50000,
        "School Loans": 12000,
        "Car Loans": 5000,
        "Credit Card Debt": 4000,
        "PayDay": 1200
        },
    "manager": {
        "Name": "Business Manager", 
        "Salary": 4600, 
        "Cashflow": 0,
        "Taxes": 900, 
        "Home Mortgage Payment": 700, 
        "School Loan Payment": 100,
        "Car Loan Payment": 100,
        "Credit Card Payment": 200,
        "Other Expenses": 1000,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 400,
        "Home Mortgage": 75000,
        "School Loans": 12000,
        "Car Loans": 6000,
        "Credit Card Debt": 4000,
        "PayDay": 1600
        },
    "doc": {
        "Name": "Doctor", 
        "Salary": 13200, 
        "Cashflow": 0,
        "Taxes": 3200, 
        "Home Mortgage Payment": 1900, 
        "School Loan Payment": 700,
        "Car Loan Payment": 300,
        "Credit Card Payment": 200,
        "Other Expenses": 2000,
        "Bank Loan Payment": 0,
        "Children": 0,
        "Savings": 3500,
        "Home Mortgage": 202000,
        "School Loans": 150000,
        "Car Loans": 19000,
        "Credit Card Debt": 10000,
        "PayDay": 4900
        }
}

for slug, profession in all_professions_dict.items():
    new_profession = Profession(
        slug=slug,
        name=profession["Name"], 
        salary=profession["Salary"], 
        cashflow=profession["Cashflow"], 
        tax=profession["Taxes"], 
        home_mortgage_payment=profession["Home Mortgage Payment"], 
        school_loan_payment=profession["School Loan Payment"], 
        car_loan_payment=profession["Car Loan Payment"], 
        credit_card_payment=profession["Credit Card Payment"], 
        other_expenses=profession["Other Expenses"], 
        bank_loan_payment=profession["Bank Loan Payment"], 
        children=profession["Children"], 
        children_expenses = profession["Children"] * 380,
        savings=profession["Savings"], 
        home_mortgage=profession["Home Mortgage"], 
        school_loans=profession["School Loans"], 
        car_loans=profession["Car Loans"], 
        credit_card_debt=profession["Credit Card Debt"], 
        payday=profession["PayDay"]
        )
    db.session.add(new_profession)

db.session.commit()



# Assets

all_opportunities_list = {
        "Stock / Mutual": [
            "GRO4US",
            "MYT4U",
            "OK4U",
            "ON2U"],
        "Real Estate": [
            "Condo 2Br/1Ba", 
            "House 2Br/1Ba", 
            "House 3Br/2Ba", 
            "Duplex", 
            "4-plex", 
            "8-plex", 
            "Apartment Home"
            ],
        "Business": [
            "Auto Dealer",
            "Auto Wash",
            "Car Wash",
            "Doctor Office",
            "Laundromat",
            "Pinball Machines",
            "Pizza Chain",
            "Pizza Franchise",
            "Sandwich Shop"
        ]
}

for category, list in all_opportunities_list.items():
    for type in list:
        new_opportunity = Opportunity(
            type = type,
            category = category,
        )
        new_opportunity.save()
    






# other_buys = {
#     "Gold": {
#         "Coin Collector Liquidates": {
#             "Coins": 5,
#             "Price": 1000,
#         },
#         "Friend Needs Fast Cash": {
#             "Coins": 10,
#             "Price": 3000,
#         }
#     }
# }