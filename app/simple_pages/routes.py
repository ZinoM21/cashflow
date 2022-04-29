from flask import Blueprint, get_flashed_messages, redirect, render_template, url_for, request, current_app, send_file

blueprint = Blueprint('simple_pages', __name__)


### ROOT ###
@blueprint.route('/')
def root():
    return render_template("simple_pages/root.html")

@blueprint.route('/home')
@blueprint.route('/start')
def root_redirect():
    return redirect(url_for('simple_pages.root'))


### FAQ ###
@blueprint.get('/faq')
def get_faq():
    return render_template('simple_pages/faq.html')

@blueprint.route('/downloads/rules')
def download_rules():
  return send_file('static/downloads/rules.pdf')


### IMPRINT ###
@blueprint.get('/imprint')
def get_imprint():
    return render_template('simple_pages/imprint.html')


### IMPRINT ###
@blueprint.get('/privacy')
def get_privacy():
    return render_template('simple_pages/privacy.html')