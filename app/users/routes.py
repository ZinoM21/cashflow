from flask import Blueprint, get_flashed_messages, redirect, render_template, url_for, request, current_app, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required, user_logged_in
#from app import simple_pages

from app.users.services.create_user import create_user
from app.users.services.change_user import change_user
from app.users.models import User

blueprint = Blueprint('users', __name__)


### SIGNUP ###
@blueprint.get('/signup')
def get_signup():
    return render_template("users/signup.html")

@blueprint.post('/signup')
def post_signup():
    try:
        # Checks
        if User.query.filter_by(email=request.form.get('email')).first():
            raise Exception ('The email address is already taken.')

        # Logic
        user = create_user(request.form)
        login_user(user)

        # View
        return redirect(url_for('users.get_account'))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        return render_template('users/signup.html', error=error)


### LOGIN ###
@blueprint.get('/login')
def get_login():
    return render_template("users/login.html")

@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(email=request.form.get('email')).first()

        # Checks
        if not user:
            raise Exception('Email address not found.')
        elif not check_password_hash(user.password, request.form.get('password')):
            raise Exception('Incorrect Password.')

        # Logic
        login_user(user)

        # View
        return redirect(url_for('users.get_account'))
    
    except Exception as error_message:
        error = error_message or 'An error occurred while logging in. Please verify your email and password.'
        return render_template('users/login.html', error=error)


### LOGOUT ####
@blueprint.get('/logout')
def get_logout():

    # Logic
    logout_user()
    
    # View
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
    # Set variables
    user = current_user

    try:
        # Checks
        if user.email == request.form.get('email'):
            raise Exception ("New email can't be old email.")
        if request.form.get('password'):
            if check_password_hash(user.password, request.form.get('password')):
                raise Exception ("New password can't be old password.")

        # Logic
        changed_user = change_user(request.form, user)

        # View
        flash('Saved changes')
        return redirect(url_for('users.get_account', user=changed_user))

    except Exception as error_message:
        error = error_message or 'An error occurred while changing user. Please make sure to enter valid data.'
        return render_template('users/account.html', user=user, error=error)

@blueprint.get('/profile')
@blueprint.get('/me')
def account_redirect():
    return redirect(url_for('users.get_account'))


### DELETE USER ###
@blueprint.get('/deleteuser')
def delete_user():
    user = current_user


    # Logic
    user.delete()
    
    # View
    flash('User deleted')
    return redirect(url_for('simple_pages.root'))