# -*- coding: utf-8 -*-

import os
import click
from flask import request, jsonify
from flask.views import MethodView

from .factory import create_app
from .blog.views import PostListCreateView, PostDetailGetUpdateDeleteView


app = create_app()

@app.cli.command()
def initdb():
    click.echo('init the db')

@app.route('/')
def hello_rest():
    return 'hello flask RESTful api'

app.add_url_rule('/posts/', view_func=PostListCreateView.as_view('posts'))
app.add_url_rule('/posts/<slug>', view_func=PostDetailGetUpdateDeleteView.as_view('post'))
