from doctest import ELLIPSIS_MARKER
from flask import Flask, redirect, url_for, render_template, send_file
from random import randint

app = Flask(__name__)
app.config.from_object('app.config')

jobs = {
    "pilot": {"name": "Pilot", "income": "8000", "tax": "3000"},
    "sanitor": {"name": "Sanitor", "income": "1500", "tax": "300"},
    "teacher": {"name": "Teacher", "income": "3000", "tax": "1000"},
    "techy": {"name": "Software Enigneer", "income": "10000", "tax": "4000"}
}

@app.route('/')
def landing():
    return render_template("landing.html")

# @app.route('/playing')
# def playing():
#     return render_template("playing.html")

@app.route('/playing/<slug>')
def playing(slug):
    return jobs[slug]

@app.route('/login')
def login():
    return render_template("login.html")