# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask.views import MethodView

from flask_mongoengine import MongoEngine


db = MongoEngine()

def create_app():
    app = Flask(__name__)

    app.config['MONGODB_SETTINGS'] = {
        'db': 'sasukekun-flask',
        'host': 'localhost',
        'port': 27017
    }

    db.init_app(app)

    return app
