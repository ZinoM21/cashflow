from flask import Blueprint, redirect, render_template, url_for
from .models import Job

blueprint = Blueprint('jobs', __name__)

# all_jobs_dict = {
#     "mechanic": {
#         "Name": "Mechanic", 
#         "Salary": "2000", 
#         "Cashflow": "0",
#         "Taxes": "400", 
#         "Home Mortgage Payment": "300", 
#         "School Loan Payment": "0",
#         "Car Loan Payment": "100",
#         "Credit Card Payment": "100",
#         "Other Expenses": "300",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "700",
#         "Home Mortgage": "31000",
#         "School Loans": "0",
#         "Car Loans": "3000",
#         "Credit Card Debt": "3000",
#         "Payday": "700"
#         },
#     "janitor": {
#         "Name": "Janitor", 
#         "Salary": "1600", 
#         "Cashflow": "0",
#         "Taxes": "300", 
#         "Home Mortgage Payment": "200", 
#         "School Loan Payment": "0",
#         "Car Loan Payment": "100",
#         "Credit Card Payment": "100",
#         "Other Expenses": "300",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "600",
#         "Home Mortgage": "20000",
#         "School Loans": "0",
#         "Car Loans": "4000",
#         "Credit Card Debt": "3000",
#         "Payday": "600"
#         },
#     "engineer": {
#         "Name": "Engineer", 
#         "Salary": "4900", 
#         "Cashflow": "0",
#         "Taxes": "1000", 
#         "Home Mortgage Payment": "700", 
#         "School Loan Payment": "100",
#         "Car Loan Payment": "200",
#         "Credit Card Payment": "200",
#         "Other Expenses": "1000",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "400",
#         "Home Mortgage": "75000",
#         "School Loans": "12000",
#         "Car Loans": "7000",
#         "Credit Card Debt": "5000",
#         "Payday": "1700"
#         },
#     "lawyer": {
#         "Name": "Lawyer", 
#         "Salary": "7500", 
#         "Cashflow": "0",
#         "Taxes": "1800", 
#         "Home Mortgage Payment": "1100", 
#         "School Loan Payment": "300",
#         "Car Loan Payment": "200",
#         "Credit Card Payment": "200",
#         "Other Expenses": "1500",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "2000",
#         "Home Mortgage": "115000",
#         "School Loans": "78000",
#         "Car Loans": "11000",
#         "Credit Card Debt": "7000",
#         "Payday": "2400"
#         },
#     "officer": {
#         "Name": "Police Officer", 
#         "Salary": "3000", 
#         "Cashflow": "0",
#         "Taxes": "600", 
#         "Home Mortgage Payment": "400", 
#         "School Loan Payment": "0",
#         "Car Loan Payment": "100",
#         "Credit Card Payment": "100",
#         "Other Expenses": "700",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "500",
#         "Home Mortgage": "46000",
#         "School Loans": "0",
#         "Car Loans": "5000",
#         "Credit Card Debt": "3000",
#         "Payday": "1100"
#         },
#     "pilot": {
#         "Name": "Airline Pilot", 
#         "Salary": "9500", 
#         "Cashflow": "0",
#         "Taxes": "2000", 
#         "Home Mortgage Payment": "1000", 
#         "School Loan Payment": "0",
#         "Car Loan Payment": "300",
#         "Credit Card Payment": "700",
#         "Other Expenses": "2000",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "2500",
#         "Home Mortgage": "90000",
#         "School Loans": "0",
#         "Car Loans": "15000",
#         "Credit Card Debt": "22000",
#         "Payday": "3500"
#         },
#     "trucker": {
#         "Name": "Truck Driver", 
#         "Salary": "2500", 
#         "Cashflow": "0",
#         "Taxes": "500", 
#         "Home Mortgage Payment": "400", 
#         "School Loan Payment": "0",
#         "Car Loan Payment": "100",
#         "Credit Card Payment": "100",
#         "Other Expenses": "600",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "800",
#         "Home Mortgage": "38000",
#         "School Loans": "0",
#         "Car Loans": "4000",
#         "Credit Card Debt": "3000",
#         "Payday": "800"
#         },
    
#     "teacher": {
#         "Name": "Teacher (K-12)", 
#         "Salary": "3300", 
#         "Cashflow": "0",
#         "Taxes": "500", 
#         "Home Mortgage Payment": "500", 
#         "School Loan Payment": "100",
#         "Car Loan Payment": "100",
#         "Credit Card Payment": "200",
#         "Other Expenses": "700",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "400",
#         "Home Mortgage": "50000",
#         "School Loans": "12000",
#         "Car Loans": "5000",
#         "Credit Card Debt": "4000",
#         "Payday": "1200"
#         },
#     "manager": {
#         "Name": "Business Manager", 
#         "Salary": "4600", 
#         "Cashflow": "0",
#         "Taxes": "900", 
#         "Home Mortgage Payment": "700", 
#         "School Loan Payment": "100",
#         "Car Loan Payment": "100",
#         "Credit Card Payment": "200",
#         "Other Expenses": "1000",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "400",
#         "Home Mortgage": "75000",
#         "School Loans": "12000",
#         "Car Loans": "6000",
#         "Credit Card Debt": "4000",
#         "Payday": "1600"
#         },
#     "doc": {
#         "Name": "Doctor", 
#         "Salary": "13200", 
#         "Cashflow": "0",
#         "Taxes": "3200", 
#         "Home Mortgage Payment": "1900", 
#         "School Loan Payment": "700",
#         "Car Loan Payment": "300",
#         "Credit Card Payment": "200",
#         "Other Expenses": "2000",
#         "Bank Loan Payment": "0",
#         "Expenses by Children": "0",
#         "Savings": "3500",
#         "Home Mortgage": "202000",
#         "School Loans": "150000",
#         "Car Loans": "19000",
#         "Credit Card Debt": "10000",
#         "Payday": "4900"
#         }
# }

@blueprint.route('/jobs')
def choose_job():
    #Log:
    print('CHOOSE YOUR JOB')

    all_jobs = Job.query.all()
    return render_template("jobs/choose_job.html", all_jobs=all_jobs)

@blueprint.route('/play')
def play():
    # Log:
    print('REDIRECT /play TO /jobs')

    return redirect(url_for('jobs.choose_job'))

@blueprint.route('/jobs/<slug>')
def job_dynamic(slug):
    # Log:
    print(F'CHOSE {all_jobs_dict[slug]["Name"].upper()} AS JOB, HERE ARE YOUR STATS')

    # Set variables for the template:
    job_dict = all_jobs_dict[slug]
    job_keys_list = list(job_dict.keys())

    return render_template("jobs/job_dynamic.html", job=slug, all_jobs_dict=all_jobs_dict, job_dict=job_dict, job_keys_list=job_keys_list)