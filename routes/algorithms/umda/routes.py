from flask import Blueprint

umda_api = Blueprint("umda_api", __name__)


@umda_api.route("/info", methods=["GET"])
def info():
    return "Hello World!"


@umda_api.route("/solve", methods=["POST"])
def solve():
    return "Hello World!"
