# coding=utf-8
__author__ = 'Mervin'
import datetime

from django.test import TestCase

from portal.utils import generate_random_string


# 单元测试类
class UnitTest(TestCase):
    def test_random_string(self):
        """
        测试随机字符串生成
        :return:
        """
        # 生成100个16位随机字符串
        count = 10000
        result_list = []
        before_generate = datetime.datetime.now()
        for i in range(0, count, 1):
            random_string = generate_random_string(16)
            result_list.append(random_string)
        after_generate = datetime.datetime.now()
        generate_cost = after_generate - before_generate
        print('Generate cost:' + str(generate_cost.microseconds / 1000) + 'ms')
        # 检查字符串是否有重复
        list_count = len(result_list)
        for x in range(0, list_count - 1, 1):
            for y in range(x, list_count - 1, 1):
                if result_list[x] == result_list[y + 1]:
                    print('Fail')
                    return
        print('Pass')
        return
