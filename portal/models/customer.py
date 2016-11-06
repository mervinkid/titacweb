# -*- coding: utf-8 -*-
from django.db import models
from .base import BaseManager
from .misc import Media


class CustomerManager(BaseManager):
    def get_all_customer(self, order='title'):
        """
        获取所有客户信息
        :return:
        """
        return self.query().all().order_by(order)

    def get_customer_by_id(self, customer_id):
        """
        通过主键查询数据
        :param customer_id:
        :return:
        """
        try:
            return self.query().get(id=customer_id)
        except Exception as e:
            print((str(e)))
            return None


class Customer(models.Model):
    """
    管理客户信息
    """
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='客户名称',
        verbose_name='客户'
    )
    fullname = models.CharField(
        db_column='fullname',
        max_length=250,
        null=True,
        blank=True,
        help_text='客户全称',
        verbose_name='全称',
    )
    logo = models.ForeignKey(
        Media,
        db_column='logo',
        null=True,
        blank=True,
        help_text='120x40规格png图像',
        verbose_name='LOGO'
    )
    objects = CustomerManager()

    def __str__(self):
        return \
            self.title

    class Meta:
        db_table = 'portal_customer'
        verbose_name_plural = '客户信息'
