# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask.views import MethodView
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from .json_response import JSONResponse
db = MongoEngine()

def create_app():
    app = Flask(__name__)

    app.response_class = JSONResponse

    app.config.from_object('sasukekun_flask.config')

    db.init_app(app)

    CORS(app)

    return app
