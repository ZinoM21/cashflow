from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin

class User(db.Model, CRUDMixin, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(80), index = True, unique = True)
    password = db.Column(db.String(120))
    uname = db.Column(db.String(80))
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))