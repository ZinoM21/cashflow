from app.users.models import User
from werkzeug.security import generate_password_hash

def change_user(form_data, user):
    # Change email of db record
    if form_data.get('email'):
        user.email=form_data.get('email')

    # Change password of db record
    if form_data.get('password'):
        user.password=generate_password_hash(form_data.get('password'))
    
    user.save()

    return user