from flask import Blueprint
from routes.warmup.routes import warmup_api
from routes.algorithms.routes import algorithms_api

api = Blueprint("api", __name__)

api.register_blueprint(warmup_api, url_prefix="/warmup")
api.register_blueprint(algorithms_api, url_prefix="/algorithms")
