from flask import Blueprint, redirect, render_template, url_for, request, current_app
from app.simple_pages.services.create_user import create_user

blueprint = Blueprint('simple_pages', __name__)


### ROOT ###

@blueprint.route('/')
def root():
    return render_template("simple_pages/root.html")

@blueprint.route('/home')
def home():
    return redirect(url_for('simple_pages.root'))


### LOGIN ###

@blueprint.get('/login')
def get_login():
    return render_template("simple_pages/login.html")

@blueprint.post('/login')
def post_login():
    return render_template("simple_pages/login.html")


### SIGNUP

@blueprint.route('/signup')
def get_signup():
    return render_template("simple_pages/signup.html")


### ACCOUNT ###

@blueprint.get('/account')
def get_account():
    return render_template("simple_pages/account.html")

@blueprint.post('/account')
def post_account():
    try:
        create_user(request.form)
        return render_template("simple_pages/account.html")

    except Exception as error_message:
        error = error_message or 'An error occurred while signing up. Please make sure to enter valid data.'
        
        current_app.logger.info(f'Error sign up: {error}')

        return render_template('simple_pages/signup.html', error=error)


### FAQ ###

@blueprint.get('/faq')
def get_faq():
    return render_template('simple_pages/faq.html')

