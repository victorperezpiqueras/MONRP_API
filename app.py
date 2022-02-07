from flask import Flask
from routes.routes import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")


@app.route("/")
def index():
    return "Hello World!"
