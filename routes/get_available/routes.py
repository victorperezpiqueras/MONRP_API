from flask import Blueprint, jsonify

from routes.algorithms.geneticnds.info_get import info_get as info_get_geneticnds
from routes.algorithms.nsgaii.info_get import info_get as info_get_nsgaii
from routes.algorithms.grasp.info_get import info_get as info_get_grasp
from routes.algorithms.umda.info_get import info_get as info_get_umda
from routes.algorithms.pbil.info_get import info_get as info_get_pbil
from routes.algorithms.mimic.info_get import info_get as info_get_mimic
from routes.algorithms.feda.info_get import info_get as info_get_feda

get_available_api = Blueprint("get_available_api", __name__)


@get_available_api.route("", methods=["GET"])
def get_available():
    available_algorithms = []
    available_algorithms.append(info_get_geneticnds())
    available_algorithms.append(info_get_nsgaii())
    available_algorithms.append(info_get_grasp())
    available_algorithms.append(info_get_umda())
    available_algorithms.append(info_get_pbil())
    available_algorithms.append(info_get_mimic())
    # available_algorithms.append(info_get_feda())

    return jsonify(available_algorithms), 200
