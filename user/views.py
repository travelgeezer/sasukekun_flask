# -*- coding: utf-8 -*-

from flask import request, Blueprint
from sasukekun_flask.utils import v1, format_response
from .models import User
user = Blueprint('user', __name__)

@user.route(v1('/user/'), methods=['GET'])
def user_info():
    if request.method == 'GET':
        users = User.objects.all()
        data = [user.json for user in users]
        return format_response(data=data)


@user.route(v1('/register/'), methods=['POST'])
def register():
    if request.method == 'POST':
        # TODO: fix not params error
        data = request.get_json()
        name = data.get('name')
        password = data.get('password')
        print('name ', name)
        print('password ', password)
        if not name:
            return format_response(code=400, info='name is needed in request data')

        if not password:
            return format_response(code=400, info='password is needed in request data')

        try:
            User.objects.get(name=name)
            return format_response(code=409, info='user exist')
        except User.DoesNotExist:
            pass

        user = User()
        user.name = name
        user.password = user.encryption(password)

        user.save()

        return format_response(data=user.json)



@user.route(v1('/login/'), methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        password = data.get('password')
        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            return format_response(code=404, info='user does not exist')

        if user.verify(password):
            return format_response(data=user.json)
        else:
            return format_response(code=400, info='name or password error')
