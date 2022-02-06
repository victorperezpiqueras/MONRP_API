from flask import Blueprint

geneticnds_api = Blueprint("geneticnds_api", __name__)


@geneticnds_api.route("/info", methods=["GET"])
def info():
    return "Hello World!"


@geneticnds_api.route("/solve", methods=["POST"])
def solve():
    return "Hello World!"
