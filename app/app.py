from flask import Flask, redirect, url_for, render_template, send_file
from . import jobs, simple_pages

app = Flask(__name__)
app.config.from_object('app.config')

# Blueprints
app.register_blueprint(jobs.routes.blueprint)
app.register_blueprint(simple_pages.routes.blueprint)