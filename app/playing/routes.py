from flask import Blueprint, redirect, render_template, url_for, request
from app.professions.models import Profession

blueprint = Blueprint('playing', __name__)

### SETUP THE GAME ###
@blueprint.route('/setup')
def setup():

    all_profs = Profession.query.all()
    prof_names = []
    for prof in all_profs:
        prof_names.append(prof.name)

    return render_template("playing/setup.html", all_profs=all_profs, prof_names=prof_names)


### START THE GAME ###
@blueprint.route('/play')
def play():
    return render_template("playing/play.html")