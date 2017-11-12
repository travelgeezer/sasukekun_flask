import os
import uuid
import cropresize2
import short_url
from flask import request
from PIL import Image
from datetime import datetime
from sasukekun_flask.ext import db
from sasukekun_flask.utils import base_url
from sasukekun_flask.config import API_IMAGE
from .utils import get_file_path, get_file_md5
from .mimes import AUDIO_MIMES, IMAGE_MIMES, VIDEO_MIMES

class PasteFile(db.Document):
    filename = db.StringField(max_length=5000, required=True)
    filehash = db.StringField(max_length=128, required=True, unique=True)
    filemd5 = db.StringField(max_length=128, required=True, unique=True)
    uploadtime = db.DateTimeField(required=True)
    mimetype = db.StringField(max_length=256, required=True)
    size = db.IntField(required=True)


    def __init__(self, filename='', mimetype='application/octet-stream',
                 size=0, filehash=None, filemd5=None, *args, **kwargs):
        super(db.Document, self).__init__(*args, **kwargs)
        self.uploadtime = datetime.now()
        self.mimetype = mimetype
        self.size = int(size)
        self.filehash = filehash if filehash else self._hash_filename(filename)
        self.filename = filename if filename else self.filehash
        self.filemd5 = filemd5

    @staticmethod
    def _hash_filename(filename):
        _, _, suffix = filename.rpartition('.')
        return '%s.%s' % (uuid.uuid4().hex, suffix)

    @classmethod
    def rsize(cls, old_paste, width, height):
        assert old_paste.is_image, TypeError('Unsupported Image Type.')

        img = cropresize2.crop_resize(
            Image.open(old_paste.path), (int(width)), (int(height))
        )

        rst = cls(filename=old_paste.filename,
                  mimetype=old_paste.mimetype)

        img.save(rst.path)
        filestat = os.stat(rst.path)
        rst.size = filestat.st_size
        return rst

    @classmethod
    def get_by_md5(cls, filemd5):
        try:
            return cls.objects.get(filemd5=filemd5)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_by_filehash(cls, filehash, code=404):
        print(cls.objects.get(filehash=filehash).path)
        return cls.objects.get(filehash=filehash)

    @classmethod
    def create_by_uploaded_file(cls, uploaded_file):
        rst = cls(filename=uploaded_file.filename,
                  mimetype=uploaded_file.mimetype)
        uploaded_file.save(rst.path)
        with open(rst.path, 'rb') as f:
            filemd5 = get_file_md5(f)
            uploaded_file = cls.get_by_md5(filemd5)
            if uploaded_file:
                os.remove(rst.path)
                return uploaded_file
            print('rst path:', rst.path)
            filestat = os.stat(rst.path)
            rst.size = filestat.st_size
            rst.filemd5 = filemd5
        return rst


    def get_url(self, subtype):
        return 'http://{host}{subtype}{filehash}'.format(
            subtype=base_url(subtype, base=API_IMAGE),
            host=request.host,
            filehash=self.filehash
        )

    def to_dict(self):
        file_dict = {}

        file_dict['id'] = str(self.id)
        file_dict['image_url'] = self.image_url
        file_dict['filename'] = self.filename
        file_dict['filehash'] = self.filehash
        file_dict['filemd5'] = self.filemd5
        file_dict['uploadtime'] = self.uploadtime
        file_dict['mimetype'] = self.mimetype
        file_dict['size'] = self.size

        return file_dict

    @property
    def image_url(self):
        return self.get_url('/upload/')

    @property
    def path(self):
        return get_file_path(self.filehash)

    @property
    def is_image(self):
        return self.mimetype in IMAGE_MIMES

    @property
    def is_audio(self):
        return self.mimetype in AUDIO_MIMES

    @property
    def is_video(self):
        return self.mimetype in VIDEO_MIMES

    @property
    def is_pdf(self):
        return self.mimetype in 'application/pdf'

    @property
    def type(self):
        for t in ('image', 'audio', 'video', 'pdf'):
            if getattr(self, 'is_' + t):
                return t
        return 'binary'
