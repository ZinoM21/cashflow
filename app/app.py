from doctest import ELLIPSIS_MARKER
from flask import Flask, redirect, url_for, render_template, send_file
from random import randint

app = Flask(__name__)
app.config.from_object('app.config')

@app.route('/landing')
def landing():
    return render_template("landing.html")

@app.route('/playing')
def playing():
    return render_template("playing.html")