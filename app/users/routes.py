from flask import Blueprint, get_flashed_messages, redirect, render_template, url_for, request, current_app, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required, user_logged_in
#from app import simple_pages

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
        
        login_user(user)
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

        user = create_user(request.form)
        login_user(user)
        return redirect(url_for('users.get_account'))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        return render_template('users/signup.html', error=error)



### LOGOUT ####

@blueprint.get('/logout')
def get_logout():
    logout_user()
    
    flash('User Logged Out')

    return redirect(url_for('simple_pages.root'))


### ACCOUNT ###

@blueprint.get('/account')
@login_required
def get_account():
    user = current_user
    return render_template("users/account.html", user=user)

@blueprint.post('/account')
def post_account():
    user = current_user
    return "yes"
