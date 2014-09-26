#coding=utf-8
__author__ = 'Mervin'
from django.db import models


class GlobalSettingManager(models.Manager):
    def get_settings(self):
        """
        获取所有设置信息并将结果以字典形式返回
        :return:
        """
        setting_list = self.get_queryset().all()
        settings = {}
        for setting_item in setting_list:
            settings[setting_item.key] = setting_item.value
        return settings


class SlideManager(models.Manager):
    def get_enabled_slide(self):
        """
        获取所有处于有效状态的Slide数据并按更新时间排序
        :return:
        """
        return self.get_queryset().filter(enable=1).order_by('-update')


class PartnerManager(models.Manager):
    def get_partners(self):
        """
        获取所有合作伙伴信息
        :return:
        """
        return self.get_queryset().all()

    def get_partner_by_id(self, partner_id):
        """
        使用主键查询数据
        :param partner_id:
        :return:
        """
        try:
            return self.get_queryset().get(id=partner_id)
        except Exception, e:
            print str(e)
            return None


class CustomerManager(models.Manager):
    def get_all_customer(self):
        """
        获取所有客户信息
        :return:
        """
        return self.get_queryset().all().order_by('title')

    def get_customer_by_id(self, customer_id):
        """
        通过主键查询数据
        :param customer_id:
        :return:
        """
        try:
            return self.get_queryset().get(id=customer_id)
        except Exception, e:
            print(str(e))
            return None


class SolutionManager(models.Manager):
    def get_enabled_solution(self):
        """
        获取所有处于有效状态的数据
        :return:
        """
        return self.get_queryset().filter(enable=1)

    def get_solution_by_id(self, solution_id):
        """
        使用主键查询数据
        :param solution_id:
        :return:
        """
        try:
            return self.get_queryset().get(id=solution_id)
        except Exception, e:
            print str(e)
            return None

    def get_search(self, query_list):
        """
        多词模糊搜索
        :param query_list:
        :return:
        """
        query_result = []
        #对query_list中的关键词项遍历筛选
        #查询项为title,keyword,sketch
        for i in range(0, len(query_list), 1):
            query_item = query_list[i]
            if i == 0:
                #第一次遍历
                #进行全新查询
                query_result = self.get_queryset().filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(keyword__icontains=query_item) |
                    models.Q(sketch__icontains=query_item),
                    enable=1
                )
            else:
                #第N次遍历
                #对上一次遍历的结果进行筛选
                query_result = query_result.filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(keyword__icontains=query_item) |
                    models.Q(sketch__icontains=query_item),
                    enable=1
                )
        return query_result


class SolutionContentManager(models.Manager):
    def get_content_by_solution_id(self, solution_id):
        """
        使用主键查询数据
        :param solution_id:
        :return:
        """
        return self.get_queryset().filter(solution=solution_id).order_by('position')

    def get_search(self, query_list):
        """
        多词模糊搜索
        :param query_list:
        :return:
        """
        query_result = []
        #对query_list中的关键词项遍历筛选
        #查询项为title,content
        for i in range(0, len(query_list), 1):
            query_item = query_list[i]
            if i == 0:
                #第一次遍历
                #进行全新查询
                query_result = self.get_queryset().filter(
                    models.Q(title__icontains=query_item) | models.Q(content__icontains=query_item))
            else:
                #第N次遍历
                #对上一次遍历的结果进行筛选
                query_result = query_result.filter(
                    models.Q(title__icontains=query_item) | models.Q(content__icontains=query_item))
        return query_result


class ProductManager(models.Manager):
    def get_enabled_product(self):
        """
        获取所有处于有效状态的数据
        :return:
        """
        return self.get_queryset().filter(enable=1)

    def get_product_by_id(self, product_id):
        """
        使用主键查询数据
        :param product_id:
        :return:
        """
        try:
            return self.get_queryset().get(id=product_id)
        except Exception, e:
            print str(e)
            return None

    def get_search(self, query_list):
        """
        多词模糊搜索
        :param query_list:
        :return:
        """
        query_result = []
        #对query_list中的关键词项遍历筛选
        #查询项为title,keyword,sketch
        for i in range(0, len(query_list), 1):
            query_item = query_list[i]
            if i == 0:
                #第一次遍历
                #进行全新查询
                query_result = self.get_queryset().filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(keyword__icontains=query_item) |
                    models.Q(sketch__icontains=query_item),
                    enable=1
                )
            else:
                #第N次遍历
                #对上一次遍历的结果进行筛选
                query_result = query_result.filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(keyword__icontains=query_item) |
                    models.Q(sketch__icontains=query_item),
                    enable=1
                )
        return query_result


class ProductContentManager(models.Manager):
    def get_content_by_product_id(self, product_id):
        """
        使用产品查询关联内容
        :param product_id:
        :return:
        """
        return self.get_queryset().filter(product=product_id).order_by('position')

    def get_search(self, query_list):
        """
        多词模糊搜索
        :param query_list:
        :return:
        """
        query_result = []
        #对query_list中的关键词项遍历筛选
        #查询项为title,content
        for i in range(0, len(query_list), 1):
            query_item = query_list[i]
            if i == 0:
                #第一次遍历
                #进行全新查询
                query_result = self.get_queryset().filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(content__icontains=query_item)
                )
            else:
                #第N次遍历
                #对上一次遍历的结果进行筛选
                query_result = query_result.filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(content__icontains=query_item)
                )
        return query_result


class ServiceManager(models.Manager):
    def get_enabled_service(self):
        """
        查询所有可用服务
        :return:
        """
        return self.get_queryset().filter(enable=1)

    def get_service_by_id(self, service_id):
        """
        通过主键查询数据
        :param service_id:
        :return:
        """
        try:
            return self.get_queryset().get(id=service_id)
        except Exception, e:
            print str(e)
            return None


class ProductCustomerManager(models.Manager):
    def get_customer_by_product_id(self, product_id):
        """
        通过产品查询客户
        :param product_id:
        :return:
        """
        return self.get_queryset().filter(product=product_id)

    def get_product_by_customer_id(self, customer_id):
        """
        通过客户查询产品
        :param customer_id:
        :return:
        """
        return self.get_queryset().filter(customer=customer_id)


class SolutionProductManager(models.Manager):
    def get_product_by_solution_id(self, solution_id):
        """
        通过解决方案id查询与其关联的产品
        :param solution_id:
        :return:
        """
        return self.get_queryset().filter(solution=solution_id)

    def get_solution_by_product_id(self, product_id):
        """
        通过产品id查询与其关联的解决方案
        :param product_id:
        :return:
        """
        return self.get_queryset().filter(product=product_id)