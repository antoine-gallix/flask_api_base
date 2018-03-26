"""Blueprint of a json service

All http errors coming from this service are json
"""

from flask import Blueprint, jsonify, current_app
from flask_json import as_json
from werkzeug.exceptions import HTTPException

service_blueprint = Blueprint('service', __name__)


@service_blueprint.route('/service')
@as_json
def service_handler():
    current_app.logger.info('calling service')
    payload = {
        'response': 1000
    }
    return payload


@service_blueprint.errorhandler(HTTPException)
def handle_error(e):
    # translates all http errors coming from this blueprint into json errors
    return jsonify(error=str(e)), e.code
