# -*- coding: utf-8 -*-

from .config import API_WEB

def base_url(url, base=API_WEB):
    u = _urljoin(base, url)
    print(u)
    return u

def _urljoin(base, url):
    if (url[0] == '/'):
        return base + url[1:]
    return base + url

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
