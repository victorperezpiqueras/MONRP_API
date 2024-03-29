from flask import Blueprint, request

from routes.algorithms.feda.info_get import info_get
from routes.algorithms.feda.solve_post import solve_post
from routes.algorithms.utils.frontend_data_parser import parse_input, parse_output

feda_api = Blueprint("feda_api", __name__)


@feda_api.route("/info", methods=["GET"])
def info():
    response = info_get()

    return {"response": response}, 200


@feda_api.route("/solve", methods=["POST"])
def solve():
    body = parse_input(request.json)
    if body["status_code"] != 200:
        return body["error"], body["status_code"]
    data = body["data"]

    algorithm, result = solve_post(data)

    response = parse_output(algorithm, result, body["data"])

    return {"response": response}, 200
