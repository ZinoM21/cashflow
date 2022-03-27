from app.extensions.database import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(25), unique=True)
    name = db.Column(db.String(20))
    salary = db.Column(db.Numeric(10, 0))
    cashflow = db.Column(db.Numeric(10, 0))
    tax = db.Column(db.Numeric(10, 0))
    home_mortgage_payment = db.Column(db.Numeric(10, 0))
    school_loan_payment = db.Column(db.Numeric(10, 0))
    car_loan_payment = db.Column(db.Numeric(10, 0))
    credit_card_payment = db.Column(db.Numeric(10, 0))
    other_expenses = db.Column(db.Numeric(10, 0))
    bank_loan_payment = db.Column(db.Numeric(10, 0))
    children = db.Column(db.Numeric(10, 0))
    children_expenses = db.Column(db.Numeric(10, 0))
    savings = db.Column(db.Numeric(10, 0))
    home_mortgage = db.Column(db.Numeric(10, 0))
    school_loans = db.Column(db.Numeric(10, 0))
    car_loans = db.Column(db.Numeric(10, 0))
    credit_card_debt = db.Column(db.Numeric(10, 0))
    payday = db.Column(db.Numeric(10, 0))
    assets = db.relationship('Assets', backref='order', lazy=True)

class Assets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20, 0))
    asset_type_id = db.Column(db.Integer, db.ForeignKey('assettypes.id'))
    cost = db.Column(db.Numeric(10, 0))
    cashflow = db.Column(db.Numeric(10, 0))
    down_payment = db.Column(db.Numeric(10, 0))

class Assettypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_type = db.Column(db.String(20, 0))

# If something was changed in the db, run a migration like this:
    # flask db migrate -m 'add picture_url to Cookie'
    # flask db upgrade
    # Important: Don't change the name of a property or remove and add properties within the same migration. Changing existing column names or removing one column and adding another within the same migration can cause issues with SQLite. This is different from other databases. But SQLite doesn't support just changing existing columns. So what you'd have to do is to use separate migrations: one for removing a column and another for adding a new column. (☝️ Note that this will mean the data within a deleted column will be lost!)

# If you want to downgrade to another migration, use this line in terminal:
    # flask db downgrade
    