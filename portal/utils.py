# coding=utf-8
__author__ = 'Mervin'
import random
import re
import string
from random import choice


def convert_to_view_value(param):
    """
    转换页面id值到数据id值
    :param param:
    :return:
    """
    try:
        data_id = int(param)
    except:
        data_id = 0
    return data_id + 1000


def convert_to_data_value(param):
    """
    转换数据id值到页面id值
    :param parm:
    :return:
    """
    try:
        page_id = int(param)
    except:
        page_id = 1000
    if page_id < 1000:
        page_id = 1000
    return page_id - 1000


def generate_random_string(length=16):
    """
    生成随机字符串
    :param length:
    :return:
    """
    chars = string.letters + string.digits
    random_string = ''.join([choice(chars) for i in range(length)])
    return random_string


def remove_html_tag(source):
    """
    移除字符串中的HTML格式标签
    :param source:
    :return:
    """
    if source:
        result = re.sub('<[^>]+>', '', source)
        return result
    else:
        return str()


def generate_string(length):
    if not isinstance(length, int):
        return ''
    if length < 1:
        return ''
    seed = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    sa = []
    for i in range(length):
        sa.append(random.choice(seed))
        salt = ''.join(sa)
    return salt
