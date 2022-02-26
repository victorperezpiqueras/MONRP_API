from flask import Blueprint, request

from routes.algorithms.nsgaii.info_get import info_get
from routes.algorithms.nsgaii.solve_post import solve_post
from routes.algorithms.utils.frontend_data_parser import parse_input, parse_output

nsgaii_api = Blueprint("nsgaii_api", __name__)


@nsgaii_api.route("/info", methods=["GET"])
def info():
    response = info_get()

    return {"response": response}, 200


@nsgaii_api.route("/solve", methods=["POST"])
def solve():
    body = parse_input(request.json)
    if body["status_code"] != 200:
        return body["error"], body["status_code"]
    data = body["data"]

    result = solve_post(data)

    response = parse_output(result, body["data"])

    return {"response": response}, 200
