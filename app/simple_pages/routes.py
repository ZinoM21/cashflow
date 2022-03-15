from flask import Blueprint, redirect, render_template, url_for

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def root():
    return render_template("simple_pages/root.html")

@blueprint.route('/home')
def home():
    return redirect(url_for('simple_pages.root'))

@blueprint.route('/login')
def login():
    return render_template("simple_pages/login.html")