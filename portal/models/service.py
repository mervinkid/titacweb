# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from .base import BaseManager


class ServiceManager(BaseManager):
    def get_enabled_service(self, order='title'):
        """
        查询所有可用服务
        :return:
        """
        return self.query().filter(enable=1).order_by(order)

    def get_service_by_id(self, service_id):
        """
        通过主键查询数据
        :param service_id:
        :return:
        """
        try:
            return self.query().get(id=service_id)
        except Exception as e:
            print((str(e)))
            return None

    def get_search(self, query_list):
        """
        多词模糊搜索
        :param query_list:
        :return:
        """
        query_result = []
        # 对query_list中的关键词项遍历筛选
        # 查询项为title,keyword,sketch
        for i in range(0, len(query_list), 1):
            query_item = query_list[i]
            if i == 0:
                # 第一次遍历
                # 进行全新查询
                query_result = self.query().filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(keyword__icontains=query_item) |
                    models.Q(sketch__icontains=query_item) |
                    models.Q(content__icontains=query_item),
                    enable=1
                )
            else:
                # 第N次遍历
                # 对上一次遍历的结果进行筛选
                query_result = query_result.filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(keyword__icontains=query_item) |
                    models.Q(sketch__icontains=query_item) |
                    models.Q(content__icontains=query_item),
                    enable=1
                )
        return query_result


class Service(models.Model):
    """
    用于管理服务数据
    """
    ENABLE_CHOICES = (
        (1, '启用'),
        (0, '禁用'),
    )
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='*标题,250个字符内',
        verbose_name='名称'
    )
    sketch = models.TextField(
        db_column='sketch',
        help_text='显示在标题之下',
        verbose_name='简介',
        null=True,
        blank=True
    )
    content = models.TextField(
        db_column='content',
        help_text='支持HTML代码',
        verbose_name='内容'
    )
    keyword = models.CharField(
        db_column='keyword',
        max_length=250,
        help_text='页面keyword信息',
        verbose_name='关键词',
        null=True,
        blank=True
    )
    update = models.DateTimeField(
        db_column='update',
        default=datetime.now(),
        editable=False,
        help_text='更新时间',
        verbose_name='更新时间'
    )
    enable = models.IntegerField(
        db_column='enable',
        default=1,
        choices=ENABLE_CHOICES,
        help_text='*启用状态',
        verbose_name='状态'
    )
    objects = ServiceManager()

    class Meta:
        db_table = 'portal_service'
        verbose_name_plural = '服务'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # 保存时自动更新数据修改时间
        self.update = datetime.now()
        return super(Service, self).save(*args, **kwargs)
