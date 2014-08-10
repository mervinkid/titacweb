#coding=utf-8
from django.test import TestCase
from portal.util import generate_random_string
from portal.models import Media

#单元测试类
class UnitTest(TestCase):
    def test_random_string(self):
        '''
        测试随机字符串生成
        :return:
        '''
        result_list = []
        for i in range(10):
            random_string = generate_random_string(16)
            result_list.append(random_string)
        print result_list
        return

class ViewTest(TestCase):
    def test_home(self):
        response = self.client.get('/')
