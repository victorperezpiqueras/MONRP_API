from flask import Flask
from routes.routes import api
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.register_blueprint(api, url_prefix="/api")
