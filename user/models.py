# -*- coding: utf-8 -*-

import json
from sasukekun_flask.ext import db


class User(db.Document):
    name = db.StringField(max_length=256, required=True)
    password= db.StringField(max_length=256, required=True)

    def __init__(self, name, password, *args, **kwargs):
        super(db.Document, self).__init__(*args, **kwargs)
        self.name = name
        self.password = self.encryption(password)


    def encryption(self, password):
        # Encrypted password
        return password

    def json(self):
        return json.dumps(self.__dict__)


    @property
    def __dict__(self):
        return {
            "name": self.name,
            "password": "I won't tell you"
        }
