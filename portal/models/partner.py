# -*- coding: utf-8 -*-
from django.db import models

from .base import BaseManager
from .misc import Media


class PartnerManager(BaseManager):
    def get_partners(self, order='title', count=10):
        """
        获取所有合作伙伴信息
        :return:
        """
        return self.query().all().order_by(order)[0:count]

    def get_partner_by_id(self, partner_id):
        """
        使用主键查询数据
        :param partner_id:
        :return:
        """
        try:
            return self.query().get(id=partner_id)
        except Exception as e:
            print((str(e)))
            return None


class Partner(models.Model):
    """
    管理合作伙伴信息
    """
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='长度限制为250个字符',
        verbose_name='合作伙伴名称'
    )
    logo = models.ForeignKey(
        Media,
        db_column='logo',
        max_length=250,
        null=True,
        blank=True,
        help_text='120x40规格png图像',
        verbose_name='LOGO'
    )
    website = models.URLField(
        db_column='website',
        null=True,
        blank=True,
        help_text='合作伙伴网址',
        verbose_name='网址'
    )
    objects = PartnerManager()

    class Meta:
        db_table = 'portal_partner'
        verbose_name_plural = '合作伙伴'

    def __str__(self):
        return \
            self.title
