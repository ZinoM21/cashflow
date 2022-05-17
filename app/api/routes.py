from flask import Blueprint, jsonify
from .services.serialize_professions import serialize_professions
from .services.serialize_opportunities import serialize_opportunities
from ..professions.models import Profession
from ..opportunities.models import Opportunity

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/professions')
def professions():
    professions = Profession.query.all()

    return jsonify(
        serialize_professions(professions)
    )

@blueprint.get('/api/v1/opportunities')
def opportunities():
    opportunities = Opportunity.query.all()

    return jsonify(
        serialize_opportunities(opportunities)
    )