from flask import Blueprint

service = Blueprint('service', __name__)

@service.route('/')
def index():
    return 'sasukekun of flask debug'
