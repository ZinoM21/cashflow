from flask import Blueprint, jsonify
from .services.serialize_professions import serialize_professions
from ..professions.models import Profession

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/professions')
def professions():
    professions = Profession.query.all()

    return jsonify(
        serialize_professions(professions)
    )