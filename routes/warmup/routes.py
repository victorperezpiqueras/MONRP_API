from flask import Blueprint

warmup_api = Blueprint("warmup_api", __name__)


@warmup_api.route("/", methods=["GET"])
def warmup_get():
    return {"response": "warmup on"}, 200
