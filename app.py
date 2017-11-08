# -*- coding: utf-8 -*-

import os
import click
from flask import request, jsonify
from flask.views import MethodView
from flask_cors import CORS
from .factory import create_app
from .blog.views import blog


app = create_app()
app.register_blueprint(blog)


@app.cli.command()
def initdb():
    click.echo('init the db')

@app.route('/')
def hello_rest():
    return 'hello flask RESTful api'

@app.route('/webAPI/test')
def test():
    return 'test web api'
