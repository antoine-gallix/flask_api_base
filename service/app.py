import logging
import logging.config
from flask import Blueprint, jsonify, Flask
import yaml
from flask_json import FlaskJSON
from service import config

# flask app name
app_name = 'service_template'

test_bp = Blueprint('test', __name__)


@test_bp.route('/test/OK')
def test_OK_handler():
    """Test endpoint to check if the app is running
    """
    return jsonify({'response': 'OK'})


@test_bp.route('/test/error')
def test_internal_error_handler():
    """Test endpoint to check internal error handling
    """
    raise Exception('internal error, sorry')


def create_app():
    """Application object factory"""

    app = Flask(__name__)

    # configure logging
    logger = app.logger
    logging.config.dictConfig(yaml.load(open('service/logging.conf')))

    # apply config
    logger.info('creating app')
    app.config.from_object(config)

    # initialize extensions
    FlaskJSON(app)

    # register blueprints
    from .service import service_blueprint
    app.register_blueprint(service_blueprint)
    app.register_blueprint(test_bp)

    # log app url map for debugging
    logger.debug(app.url_map)

    # for http errors coming from routing or generic 500 error
    # override default HTML errors with JSON errors

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(message=str(e)), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify(message=str(e)), 405

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify(message=str(e)), 500

    return app
