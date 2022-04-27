def serialize_professions(professions):
    professions_list = []

    for profession in professions:
        professions_list.append({
            "id": profession.id,
            "slug": profession.slug,
            "Name": profession.name, 
            "Salary": profession.salary, 
            "Cashflow": profession.cashflow,
            "Taxes": profession.tax, 
            "Home Mortgage Payment": profession.home_mortgage_payment, 
            "School Loan Payment": profession.school_loan_payment,
            "Car Loan Payment": profession.car_loan_payment,
            "Credit Card Payment": profession.credit_card_payment,
            "Other Expenses": profession.other_expenses,
            "Bank Loan Payment": profession.bank_loan_payment,
            "Children": profession.children,
            "Expenses of Children": profession.children_expenses, 
            "Savings": profession.savings,
            "Home Mortgage": profession.home_mortgage,
            "School Loans": profession.school_loans,
            "Car Loans": profession.car_loans,
            "Credit Card Debt": profession.credit_card_debt,
            "PayDay": profession.payday 
        })
    
    return professions_list