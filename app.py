from flask import Flask
from routes.warmup.routes import warmup_api
from routes.algorithms.routes import algorithms_api

app = Flask(__name__)

app.register_blueprint(warmup_api, url_prefix="/warmup")
app.register_blueprint(algorithms_api, url_prefix="/algorithms")


@app.route("/")
def index():
    return "Hello World!"
