from flask import Blueprint, redirect, render_template, url_for, request
from app.professions.models import Profession

blueprint = Blueprint('playing', __name__)

### START THE GAME ###
@blueprint.route('/play')
def get_play():
    return render_template("playing/play.html")