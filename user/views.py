# -*- coding: utf-8 -*-

from flask import request, Blueprint
from sasukekun_flask.utils import v1, format_response
from .models import User
user = Blueprint('user', __name__)

@user.route(v1('/user/'), methods=['GET', 'POST'])
def user_info():
    if request.method == 'GET':
        users = User.objects.all()
        data = [user.json() for user in users]
        return format_response(data=data)

    if request.method == 'POST':
        data = request.get_json()

        name = data.get('name')
        password = data.get('password')
        print('name ', name)
        print('password ', password)
        if not name:
            return format_response(code=400, info='name is needed in request data')

        if not password:
            return format_response(code=400, info='password is needed in request data')

        user = User(name, password)

        user.save()

        return format_response(data=user.json())
