# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask.views import MethodView

from flask_mongoengine import MongoEngine


db = MongoEngine()

def create_app():
    app = Flask(__name__)

    app.config.from_object('sasukekun_flask.config')

    db.init_app(app)

    return app
