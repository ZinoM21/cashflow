from flask import Blueprint, redirect, render_template, url_for, request
from .models import Profession

blueprint = Blueprint('professions', __name__)

### SEE PROFESSIONS ###
@blueprint.route('/professions')
def choose_professions():
    # Variables for template
    page_number = request.args.get('page', 1, type=int) # pagination ?
    all_professions = Profession.query.all()

    # View
    return render_template("professions/choose_profession.html", all_professions=all_professions)

@blueprint.route('/play')
def start_the_game():
    return "insert playing page here" #redirect(url_for('professions.choose_professions'))


### SINGLE PROFESSION VIEW ###
@blueprint.route('/professions/<slug>')
def profession_dynamic(slug):
    # Variables for template
    profession = Profession.query.filter_by(slug=slug).first_or_404()

    # View
    return render_template("professions/profession_dynamic.html", profession=profession)