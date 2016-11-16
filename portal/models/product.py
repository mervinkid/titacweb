# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from .base import BaseManager
from .customer import Customer
from .partner import Partner


class ProductManager(BaseManager):
    def get_enabled_product(self, order='title', count=10):
        """
        获取所有处于有效状态的数据
        :return:
        """
        return self.query().filter(enable=1).order_by(order)[0:count]

    def get_product_by_id(self, product_id):
        """
        使用主键查询数据
        :param product_id:
        :return:
        """
        try:
            return self.query().get(id=product_id)
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
                    models.Q(sketch__icontains=query_item),
                    enable=1
                )
            else:
                # 第N次遍历
                # 对上一次遍历的结果进行筛选
                query_result = query_result.filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(keyword__icontains=query_item) |
                    models.Q(sketch__icontains=query_item),
                    enable=1
                )
        return query_result


class ProductContentManager(BaseManager):
    def get_content_by_product_id(self, product_id):
        """
        使用产品查询关联内容
        :param product_id:
        :return:
        """
        return self.query().filter(product=product_id).order_by('position')

    def get_search(self, query_list):
        """
        多词模糊搜索
        :param query_list:
        :return:
        """
        query_result = []
        # 对query_list中的关键词项遍历筛选
        # 查询项为title,content
        for i in range(0, len(query_list), 1):
            query_item = query_list[i]
            if i == 0:
                # 第一次遍历
                # 进行全新查询
                query_result = self.query().filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(content__icontains=query_item)
                )
            else:
                # 第N次遍历
                # 对上一次遍历的结果进行筛选
                query_result = query_result.filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(content__icontains=query_item)
                )
        return query_result


class Product(models.Model):
    """
    用于管理产品数据
    """
    ENABLE_CHOICES = (
        (1, '启用'),
        (0, '禁用'),
    )
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='*产品标题,250个字符内',
        verbose_name='标题'
    )
    subtitle = models.CharField(
        db_column='subtitle',
        max_length=250,
        null=True,
        blank=True,
        help_text='显示在主标题之下',
        verbose_name='副标题'
    )
    enable = models.IntegerField(
        db_column='enable',
        default=1,
        choices=ENABLE_CHOICES,
        help_text='*启用状态',
        verbose_name='状态'
    )
    sketch = models.TextField(
        db_column='sketch',
        null=True,
        blank=True,
        help_text='显示在标题之下',
        verbose_name='简介'
    )
    keyword = models.CharField(
        db_column='keyword',
        max_length=250,
        null=True,
        blank=True,
        help_text='页面Keyword',
        verbose_name='关键字'
    )
    update = models.DateTimeField(
        db_column='update',
        default=datetime.now(),
        editable=False,
        help_text='*更新时间',
        verbose_name='更新时间'
    )
    partner = models.ForeignKey(
        Partner,
        db_column='partner',
        null=True,
        blank=True,
        help_text='选择产品所属合作伙伴',
        verbose_name='合作伙伴'
    )
    customers = models.ManyToManyField(
        to=Customer,
        db_column='portal_product_customer_relation',
        related_name='products',
        blank=True
    )
    objects = ProductManager()

    class Meta:
        db_table = 'portal_product'
        verbose_name_plural = '产品'

    def __str__(self):
        return \
            self.title

    def save(self, *args, **kwargs):
        # 保存时自动更新数据修改时间
        self.update = datetime.now()
        return super(Product, self).save(*args, **kwargs)


class ProductContent(models.Model):
    """
    用于管理产品内容
    """
    POSITION_CHOICES = {
        (0, '位置0'),
        (1, '位置1'),
        (2, '位置2'),
        (3, '位置3'),
        (4, '位置4'),
    }
    product = models.ForeignKey(
        Product,
        db_column='product_id',
        help_text='*选择所属产品',
        verbose_name='解决方案',
        related_name='contents'
    )
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='*内容标题,250个字符内',
        verbose_name='标题'
    )
    content = models.TextField(
        db_column='content',
        help_text='支持HTML代码',
        verbose_name='内容'
    )
    update = models.DateTimeField(
        db_column='update',
        default=datetime.now(),
        editable=False,
        help_text='更新时间',
        verbose_name='更新时间'
    )
    position = models.IntegerField(
        db_column='position',
        default=0,
        choices=POSITION_CHOICES,
        help_text='位置从左至右',
        verbose_name='位置'
    )
    objects = ProductContentManager()

    class Meta:
        db_table = 'portal_product_content'
        verbose_name_plural = '产品内容'

    def __str__(self):
        return \
            self.title

    def save(self, *args, **kwargs):
        # 保存时自动更新数据修改时间
        self.update = datetime.now()
        return super(ProductContent, self).save(*args, **kwargs)
