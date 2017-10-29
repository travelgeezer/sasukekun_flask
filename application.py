from flask import Flask, request

app = Flask(__name__)


@app.route('/api/sample-list', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def sample_list():
    if request.method == 'GET':
        return 'send request with `GET` method'
    elif request.method == 'POST':
        return 'send request with `POST` method'
    elif request.method == 'PUT':
        return 'send request with `PUT` method'
    elif request.method == 'PATCH':
        return 'send request with `PATCH` method'
    elif request.method == 'DELETE':
        return 'send request with `DELETE` method'
