from flask import Blueprint, redirect, render_template, url_for, request, current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app.users.services.create_user import create_user
from app.users.models import User

blueprint = Blueprint('users', __name__)


### LOGIN ###

@blueprint.get('/login')
def get_login():
    return render_template("users/login.html")

@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(email=request.form.get('email')).first()
        if not user:
            raise Exception('Email address not found.')
        elif check_password_hash(request.form.get('password'), user.password):
            raise Exception('Incorrect Password.')
        
        return redirect(url_for('users.get_account'))
    
    except Exception as error_message:
        error = error_message or 'An error occurred while logging in. Please verify your email and password.'
        return render_template('users/login.html', error=error)


### SIGNUP

@blueprint.get('/signup')
def get_signup():
    return render_template("users/signup.html")

@blueprint.post('/signup')
def post_signup():
    try:
        # Check for email in database & give error
        if User.query.filter_by(email=request.form.get('email')).first():
            raise Exception ('The email address is already taken.')

        create_user(request.form)
        return redirect(url_for('users.get_account'))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        return render_template('users/signup.html', error=error)



### LOGOUT ####

@blueprint.get('/logout')
def get_logout():
    return 'User logged out'


### ACCOUNT ###

@blueprint.get('/account')
def get_account():
    return render_template("users/account.html")

# @blueprint.post('/account')
# def post_account():
#     try:
#         create_user(request.form)
#         return render_template("users/account.html")

#     except Exception as error_message:
#         error = error_message or 'An error occurred while signing up. Please make sure to enter valid data.'
        
#         current_app.logger.info(f'Error sign up: {error}')

#         return render_template('users/signup.html', error=error)