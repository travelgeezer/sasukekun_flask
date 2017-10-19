from flask import Blueprint

carwler = Blueprint('carwler', __name__)

@carwler.route('/carwler')
def index():
    return 'carwler of flask'
