# -*- coding: utf-8 -*-

import json
from sasukekun_flask.ext import db, bcrypt


class User(db.Document):
    name = db.StringField(max_length=256, required=True)
    password= db.StringField(max_length=256, required=True)

    def encryption(self, password):
        # python2
        # return bcrypt.generate_password_hash(password)
        # python3
        return bcrypt.generate_password_hash(password).decode('utf-8')


    def verify(self, password):
        print('verify:')
        return bcrypt.check_password_hash(self.password, password)


    @property
    def json(self):
        return json.dumps(self.__dict__)


    @property
    def __dict__(self):
        return {
            "name": self.name,
            "password":self.password
        }
