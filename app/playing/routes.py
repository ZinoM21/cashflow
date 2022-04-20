from flask import Blueprint, redirect, render_template, url_for, request

blueprint = Blueprint('playing', __name__)

### START THE GAME ###

@blueprint.route('/play')
def play():
    return render_template("playing/play.html")