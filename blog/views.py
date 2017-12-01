# -*- coding: utf-8 -*-

from flask import request, Blueprint
from .models import Post
from sasukekun_flask.utils import v1, format_response

blog = Blueprint('blog', __name__)

@blog.route(v1('/posts/'), methods=['GET', 'POST'])
def postListAndCreateBlog():
    if request.method == 'GET':
        posts = Post.objects.all()
        category = request.args.get('category')
        tag = request.args.get('tag')

        if category:
            posts = posts.filter(category=category)

        if tag:
            posts = posts.filter(tag=tag)

        data = [post.to_dict() for post in posts]
        return format_response(data=data)

    elif request.method == 'POST':
        '''
        Send a json data as follow will create a new blog instance

        {
            "title": "Title1",
            "slug": "title-1",
            "abstract": "Abstract for this article",
            "raw": "The article content",
            "author": "geezer.",
            "category": "default",
            "tags": ["tag1", "tag2"]
        }
        '''
        data = request.get_json()
        # TODO: fix this
        try:
            post = Post.objects.get(slug=data.get('slug'))
            return format_response(code=409, info='This blog exists.')
        except Post.DoesNotExist:
            article = Post()
            article.title = data.get('title')
            article.slug = data.get('slug')
            article.abstract = data.get('abstract')
            article.raw = data.get('raw')
            article.author = data.get('author')
            article.category = data.get('category')
            article.tags = data.get('tags')

            article.save()

            return format_response(data=article.to_dict())


@blog.route(v1('/posts/<slug>/'), methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def postDetail(slug):
    if request.method == 'GET':
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return format_response(code=404, info='post does not exist')
        return format_response(data=post.to_dict())

    elif request.method == 'PUT':
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return format_response(code=404, info='post does not exist')

        data = request.get_json()

        if not data.get('title'):
            return format_response(code=400, info='title is needed in request data')

        if not data.get('slug'):
            return format_response(code=400, info='slug is needed in request data')

        if not data.get('abstract'):
            return format_response(code=400, info='abstract is needed in request data')

        if not data.get('raw'):
            return format_response(code=400, info='raw is needed in request data')

        if not data.get('author'):
            return format_response(code=400, info='author is needed in request data')

        if not data.get('category'):
            return format_response(code=400, info='category is needed in request data')

        if not data.get('tags'):
            return format_response(code=400, info='tags is needed in request data')

        post.title = data['title']
        post.slug = data['slug']
        post.abstract = data['abstract']
        post.raw = data['raw']
        post.author = data['author']
        post.category = data['category']
        post.tags = data['tags']

        post.save()

        return format_response(data=post.to_dict())

    elif request.method == 'PATCH':
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return format_response(code=404, info='post does not exist')

        data = request.get_json()

        post.title = data.get('title') or post.title
        post.slug = data.get('slug') or post.slug
        post.abstract = data.get('abstract') or post.abstract
        post.raw = data.get('raw') or post.raw
        post.author = data.get('author') or post.author
        post.category = data.get('category') or post.category
        post.tags = data.get('tags') or post.tags

        return format_response(data=post.to_dict())

    elif request.method == 'DELETE':
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return format_response(code=404, info='post does not exist')
        post.delete()

        return format_response(data='Succeed to delete post')
