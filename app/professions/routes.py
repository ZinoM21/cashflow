from flask import Blueprint, redirect, render_template, url_for, request, current_app
from .models import Profession

blueprint = Blueprint('professions', __name__)

### SEE PROFESSIONS ###
@blueprint.route('/professions')
def professions():
    # Variables for template
    page_number = request.args.get('page', 1, type=int)
    all_profs = Profession.query.all()                                                                      # returns list
    profs_pagination = Profession.query.paginate(page_number, current_app.config['PROFESSIONS_PER_PAGE'])   # returns object/class

    # View
@blueprint.route('/play')
def start_the_game():
    return "insert playing page here" #redirect(url_for('professions.professions'))

### SINGLE PROFESSION VIEW ###
@blueprint.route('/professions/<slug>')
def profession_dynamic(slug):
    # Variables for template
    profession = Profession.query.filter_by(slug=slug).first_or_404()

    # View
    return render_template("professions/profession_dynamic.html", profession=profession)