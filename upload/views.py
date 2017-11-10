from flask import request, Blueprint
from sasukekun_flask import utils
from .models import PasteFile

upload = Blueprint('upload', __name__)

@upload.route(utils.base_url('/upload/'), methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return utils.format_response(data='show file list.')
    elif request.method == 'POST':
        uploaded_file = request.files['file']
        w = request.form.get('w')
        h = request.form.get('h')
        if not uploaded_file:
            utils.format_response(code=400, info='not file')
        if False and w and h:
            paste_file = PasteFile.rsize(uploaded_file, w, h) # TODO: fix issues
        else:
            paste_file = PasteFile.create_by_uploaded_file(uploaded_file)

        paste_file.save()

        return utils.format_response(data=paste_file.to_dict())
