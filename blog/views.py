# -*- coding: utf-8 -*-

from flask import request, jsonify
from flask.views import MethodView
from .models import Post

class PostListCreateView(MethodView):
    def get(self):
        posts = Post.objects.all()
        category = request.args.get('category')
        tag = request.args.get('tag')

        if category:
            posts = posts.filter(category=category)

        if tag:
            posts = posts.filter(tag=tag)

        data = [post.to_dict() for post in posts]

        return jsonify(posts=data)

    def post(self):
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

        article = Post()
        article.title = data.get('title')
        article.slug = data.get('slug')
        article.abstract = data.get('abstract')
        article.raw = data.get('raw')
        article.author = data.get('author')
        article.category = data.get('category')
        article.tags = data.get('tags')

        article.save()

        return jsonify(article.to_dict())



class PostDetailGetUpdateDeleteView(MethodView):
    def get(self, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return jsonify({'error': 'post does not exist'}), 404

        return jsonify(post=post.to_dict())

    def put(self, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return jsonify({'error': 'post does not exist'}), 404

        data = request.get_json()

        if not data.get('title'):
            return 'title is needed in request data', 400

        if not data.get('slug'):
            return 'slug is needed in request data', 400

        if not data.get('abstract'):
            return 'abstract is needed in request data', 400

        if not data.get('raw'):
            return 'raw is needed in request data', 400

        if not data.get('author'):
            return 'author is needed in request data', 400

        if not data.get('category'):
            return 'category is needed in request data', 400

        if not data.get('tags'):
            return 'tags is needed in request data', 400


        post.title = data['title']
        post.slug = data['slug']
        post.abstract = data['abstract']
        post.raw = data['raw']
        post.author = data['author']
        post.category = data['category']
        post.tags = data['tags']

        post.save()

        return jsonify(post=post.to_dict())

    def patch(self, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return jsonify({'error': 'post does not exist'}), 404

        data = request.get_json()

        post.title = data.get('title') or post.title
        post.slug = data.get('slug') or post.slug
        post.abstract = data.get('abstract') or post.abstract
        post.raw = data.get('raw') or post.raw
        post.author = data.get('author') or post.author
        post.category = data.get('category') or post.category
        post.tags = data.get('tags') or post.tags

        return jsonify(post=post.to_dict())

    def delete(self, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return jsonify({'error': 'post does not exist'}), 404

        post.delete()

        return 'Succeed to delete post', 204
