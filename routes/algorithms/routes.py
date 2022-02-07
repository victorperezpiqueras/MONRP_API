from flask import Blueprint
from routes.algorithms.grasp.routes import grasp_api
from routes.algorithms.nsgaii.routes import nsgaii_api
from routes.algorithms.geneticnds.routes import geneticnds_api
from routes.algorithms.umda.routes import umda_api
from routes.algorithms.pbil.routes import pbil_api
from routes.algorithms.mimic.routes import mimic_api
from routes.algorithms.feda.routes import feda_api

algorithms_api = Blueprint("algorithms_api", __name__)

algorithms_api.register_blueprint(geneticnds_api, url_prefix="/geneticnds")
algorithms_api.register_blueprint(nsgaii_api, url_prefix="/nsgaii")
algorithms_api.register_blueprint(grasp_api, url_prefix="/grasp")
algorithms_api.register_blueprint(umda_api, url_prefix="/umda")
algorithms_api.register_blueprint(pbil_api, url_prefix="/pbil")
algorithms_api.register_blueprint(mimic_api, url_prefix="/mimic")
algorithms_api.register_blueprint(feda_api, url_prefix="/feda")
