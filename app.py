# -*- coding: utf-8 -*-

from .factory import create_app
from .user.views import user
from .blog.views import blog
from .upload.views import upload

app = create_app()
app.register_blueprint(user)
app.register_blueprint(blog)
app.register_blueprint(upload)

@app.route('/')
def hello_rest():
    return 'hello flask RESTful api'
