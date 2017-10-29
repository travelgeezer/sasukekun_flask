from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/sample-list', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def sample_list():
    if request.method == 'GET':
        data = {
            'code': 0,
            'data': [{'sample': 'sample data', 'list': [1, 2, 3]}],
            'info': 'ok'
        }
        return jsonify(data)
    elif request.method == 'POST':
        return 'send request with `POST` method'
    elif request.method == 'PUT':
        return 'send request with `PUT` method'
    elif request.method == 'PATCH':
        return 'send request with `PATCH` method'
    elif request.method == 'DELETE':
        return 'send request with `DELETE` method'
