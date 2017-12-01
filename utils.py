# -*- coding: utf-8 -*-

from .config import API_WEB

def verify_path(path):
    if path[0] != '/' or path[len(path) -1] != '/':
        raise ValueError('The path: "%s" format error must be in the format of "/path/"' % path)

def base_url(level, url, base=API_WEB):

    verify_path(base)
    verify_path(url)

    print(base + level + url)
    return base + level + url

def v1(url, base=API_WEB):
    return base_url(level='v1', url=url, base=base)


def format_response(code = 0, data = {}, info = 'ok'):
    """
    format response
    :param code: return status code
    :param data: return data
    :param info: return hint message
    :return :class:`dict`
    :rtype: dict
    """
    return {
        "code": code,
        "data": data,
        "info": info
    }
