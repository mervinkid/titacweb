#coding=utf-8
__author__ = 'Mervin'
import string
from random import choice

def convert_to_view_value(param):
    '''
    转换页面id值到数据id值
    :param param:
    :return:
    '''
    try:
        data_id = int(param)
    except:
        data_id = 0
    return data_id + 1000

def convert_to_data_value(param):
    '''
    转换数据id值到页面id值
    :param parm:
    :return:
    '''
    try:
        page_id = int(param)
    except:
        page_id = 1000
    if page_id < 1000:
        page_id = 1000
    return page_id - 1000

def generate_random_string(length=16):
    #生成随机字符串
    chars = string.letters + string.digits
    random_string =  ''.join([ choice(chars) for i in range(length)])
    return random_string