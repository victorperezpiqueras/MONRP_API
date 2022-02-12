from flask import Blueprint
from routes.warmup.routes import warmup_api
from routes.algorithms.routes import algorithms_api
from routes.get_available.routes import get_available_api

api = Blueprint("api", __name__)

api.register_blueprint(warmup_api, url_prefix="/warmup")
api.register_blueprint(get_available_api, url_prefix="/get_available")
api.register_blueprint(algorithms_api, url_prefix="/algorithms")
