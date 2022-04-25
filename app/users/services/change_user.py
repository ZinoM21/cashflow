from app.users.models import User
from werkzeug.security import generate_password_hash

def change_user(form_data, user):
    # Change first name of db record
    if form_data.get('fname'):
        user.fname=form_data.get('fname')

    # Change last name of db record
    if form_data.get('lname'):
        user.lname=form_data.get('lname')

    # Change username of db record
    if form_data.get('uname'):
        user.uname=form_data.get('uname')
    
    # Change email of db record
    if form_data.get('email'):
        user.email=form_data.get('email')

    # Change password of db record
    if form_data.get('pw_new'):
        user.password=generate_password_hash(form_data.get('pw_new'))
    
    user.save()

    return user