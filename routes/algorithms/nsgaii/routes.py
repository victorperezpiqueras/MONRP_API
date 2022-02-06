from flask import Blueprint

nsgaii_api = Blueprint("nsgaii_api", __name__)


@nsgaii_api.route("/info", methods=["GET"])
def info():
    return "Hello World!"


@nsgaii_api.route("/solve", methods=["POST"])
def solve():
    return "Hello World!"
