# -*- coding: utf-8 -*-
import json
from datetime import datetime
from sasukekun_flask.ext import db

class Post(db.Document):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True, unique=True)
    abstract = db.StringField()
    raw = db.StringField(required=True)
    pub_time = db.DateTimeField()
    update_time = db.DateTimeField()
    author = db.StringField()
    category = db.StringField(max_length=64)
    tags = db.ListField(db.StringField(max_length=30))


    def save(self, *args, **kw):
        now = datetime.now()
        if not self.pub_time:
            self.pub_time = now
            self.update_time = now

        return super(Post, self).save(*args, **kw)

    @property
    def __dict__(self):
        return {
            'title': self.title,
            'slug': self.slug,
            'abstract': self.abstract,
            'raw': self.raw,
            'pub_time': self.pub_time,
            'update_time': self.update_time,
            'author': self.author,
            'category': self.category,
            'tags': self.tags
        }

    @property
    def json(self):
        return json.dumps(self.__dict__)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__

    mate = {
        'allow_inheritance': True,
        'indexes': ['slug'],
        'ordering': ['-pub_time']
    }
