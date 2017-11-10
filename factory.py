# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_cors import CORS
from .ext import db
from .json_response import JSONResponse


def create_app():
    app = Flask(__name__)

    app.response_class = JSONResponse

    app.config.from_object('sasukekun_flask.config')

    db.init_app(app)

    CORS(app)

    return app
