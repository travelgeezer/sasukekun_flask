from flask import request, Blueprint, send_file
from sasukekun_flask.utils import v1, format_response
from sasukekun_flask.config import API_IMAGE
from .models import PasteFile

ONE_MONTH = 60 * 60 * 24 * 30

upload = Blueprint('upload', __name__)

@upload.route(v1('/upload/'), methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        paste_files = PasteFile.objects.all()
        data = [paste_file.to_dict() for paste_file in paste_files]
        return format_response(data=data)

    elif request.method == 'POST':
        uploaded_file = request.files['file']
        w = request.form.get('w')
        h = request.form.get('h')
        if not uploaded_file:
            format_response(code=400, info='not file')
        if False and w and h:
            paste_file = PasteFile.rsize(uploaded_file, w, h) # TODO: fix issues
        else:
            paste_file = PasteFile.create_by_uploaded_file(uploaded_file)

        paste_file.save()

        return format_response(data=paste_file.to_dict())


@upload.route(v1('/upload/<filehash>/', base=API_IMAGE),
              methods=['GET'])
def download(filehash):
    paste_file = PasteFile.get_by_filehash(filehash)

    return send_file(
        open(paste_file.path, 'rb'),
        mimetype='application/octet-stream',
        cache_timeout=ONE_MONTH,
        as_attachment=True,
        attachment_filename=paste_file.filename.encode('utf-8'))
