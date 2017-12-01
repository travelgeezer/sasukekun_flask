# -*- coding: utf-8 -*-

from .config import API_WEB

def base_url(level, url, base=API_WEB):
    if (url[0] != '/' or url[len(url) -1] != '/'):
        raise ValueError('The url format error must be in the format of "/url/"')
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
