# -*- coding: utf-8 -*-

def base_url(url, base='/webAPI/'):
    u = _urljoin(base, url)
    print(u)
    return u

def _urljoin(base, url):
    return base + url.replace('/', '', 1)

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
