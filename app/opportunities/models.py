from unicodedata import name
from app.extensions.database import db, CRUDMixin

class Opportunity(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(80))
    category = db.Column(db.String(80))

