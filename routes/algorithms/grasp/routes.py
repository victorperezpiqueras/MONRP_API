from flask import Blueprint

grasp_api = Blueprint("grasp_api", __name__)


@grasp_api.route("/info", methods=["GET"])
def info():
    return "Hello World!"


@grasp_api.route("/solve", methods=["POST"])
def solve():
    return "Hello World!"
