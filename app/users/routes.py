from flask import Blueprint, redirect, render_template, url_for, request, current_app
from app.users.services.create_user import create_user

blueprint = Blueprint('users', __name__)


### LOGIN ###

@blueprint.get('/login')
def get_login():
    return render_template("users/login.html")

@blueprint.post('/login')
def post_login():
    return 'User logged in'


### SIGNUP

@blueprint.get('/signup')
def get_signup():
    return render_template("users/signup.html")

@blueprint.post('/signup')
def post_signup():
    return 'User created'


### LOGOUT ####

@blueprint.get('/logout')
def get_logout():
    return 'User logged out'


### ACCOUNT ###

@blueprint.get('/account')
def get_account():
    return render_template("users/account.html")

@blueprint.post('/account')
def post_account():
    try:
        create_user(request.form)
        return render_template("users/account.html")

    except Exception as error_message:
        error = error_message or 'An error occurred while signing up. Please make sure to enter valid data.'
        
        current_app.logger.info(f'Error sign up: {error}')

        return render_template('users/signup.html', error=error)