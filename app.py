# -*- coding: utf-8 -*-

import os
import click
from flask import request, jsonify
from flask.views import MethodView

from .factory import create_app

app = create_app()

from .blog.views import PostListCreateView, PostDetailGetUpdateDeleteView, postList




@app.cli.command()
def initdb():
    click.echo('init the db')

@app.route('/')
def hello_rest():
    return 'hello flask RESTful api'

@app.route('/webAPI/test')
def test():
    return 'test web api'


#app.add_url_rule('/webAPI/posts/', view_func=PostListCreateView.as_view('posts'))
app.add_url_rule('/webAPI/posts/<slug>', view_func=PostDetailGetUpdateDeleteView.as_view('post'))
