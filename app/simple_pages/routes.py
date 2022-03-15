from flask import Blueprint, redirect, render_template, url_for

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def landing():
    return render_template("simple_pages/index.html")

@blueprint.route('/home')
def home():
    return redirect(url_for('simple_pages.landing'))

@blueprint.route('/login')
def login():
    return render_template("simple_pages/login.html")