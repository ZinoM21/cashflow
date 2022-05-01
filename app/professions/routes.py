from flask import Blueprint, redirect, render_template, url_for, request, current_app
from .models import Profession

blueprint = Blueprint('professions', __name__)


### ------- SEE PROFESSIONS PAGINATED ------- ###
@blueprint.route('/professions')
def professions():

    # Set Variables
    page_number = request.args.get('page', 1, type=int)
    profs_pagination = Profession.query.paginate(page_number, current_app.config['PROFESSIONS_PER_PAGE'])

    # View
    return render_template("professions/professions.html", profs_pagination=profs_pagination)

# Redirect
@blueprint.route('/jobs')
def redirect_professions():
    return redirect(url_for('professions.professions'))


### ------- SINGLE PROFESSION VIEW ------- ###
@blueprint.route('/professions/<slug>')
def profession_dynamic(slug):

    # Set Variables
    profession = Profession.query.filter_by(slug=slug).first_or_404()

    # View
    return render_template("professions/profession_dynamic.html", profession=profession)

# Redirect
@blueprint.route('/jobs/<slug>')
def redirect_profession_dynamic(slug):
    return redirect(url_for('professions.profession_dynamic', slug=slug))