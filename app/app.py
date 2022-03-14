from doctest import ELLIPSIS_MARKER
from flask import Flask, redirect, url_for, render_template, send_file
from random import randint
from . import jobs

app = Flask(__name__)
app.config.from_object('app.config')
app.register_blueprint(jobs.routes.blueprint)

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/login')
def login():
    return render_template("login.html")