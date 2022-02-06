from flask import Blueprint, jsonify, request
from routes.algorithms.geneticnds.info_get import info_get

from routes.algorithms.parse_body import parse_body

from routes.algorithms.geneticnds.solve_post import solve_post

geneticnds_api = Blueprint("geneticnds_api", __name__)


@geneticnds_api.route("/info", methods=["GET"])
def info():
    response = info_get()

    return {"response": response}, 200


@geneticnds_api.route("/solve", methods=["POST"])
def solve():
    body = parse_body(request.json)
    if body["status_code"] != 200:
        return body["error"]
    data = body["data"]

    response = solve_post(data)

    return {"response": response}, 200
