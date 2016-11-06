# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from .base import BaseManager
from .product import Product


class SolutionManager(BaseManager):
    def get_enabled_solution(self, order='title'):
        """
        获取所有处于有效状态的数据
        :return:
        """
        return self.query().filter(enable=1).order_by(order)

    def get_solution_by_id(self, solution_id):
        """
        使用主键查询数据
        :param solution_id:
        :return:
        """
        try:
            return self.query().get(id=solution_id)
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


class Solution(models.Model):
    """
    用于管理解决方案信息
    """
    ENABLE_CHOICES = (
        (1, '启用'),
        (0, '禁用'),
    )
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='*解决方案标题',
        verbose_name='标题'
    )
    subtitle = models.CharField(
        db_column='subtitle',
        max_length=250,
        null=True,
        blank=True,
        help_text='解决方案副标题',
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
        help_text='显示在标题下',
        verbose_name='简介'
    )
    keyword = models.CharField(
        db_column='keyword',
        max_length=250,
        null=True,
        blank=True,
        help_text='页面keyword属性',
        verbose_name='关键字'
    )
    update = models.DateTimeField(
        db_column='update',
        default=datetime.now(),
        editable=False, help_text='*更新时间',
        verbose_name='更新时间'
    )
    products = models.ManyToManyField(
        to=Product,
        db_column='portal_solution_product_relation',
        related_name='solutions',
        blank=True
    )
    objects = SolutionManager()

    class Meta:
        db_table = 'portal_solution'
        verbose_name_plural = '解决方案'

    def __str__(self):
        return \
            self.title

    def save(self, *args, **kwargs):
        # 保存时自动更新数据修改时间
        self.update = datetime.now()
        return super(Solution, self).save(*args, **kwargs)


class SolutionContentManager(BaseManager):
    def get_content_by_solution_id(self, solution_id):
        """
        使用主键查询数据
        :param solution_id:
        :return:
        """
        return self.query().filter(solution=solution_id).order_by('position')

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
                    models.Q(content__icontains=query_item))
            else:
                # 第N次遍历
                # 对上一次遍历的结果进行筛选
                query_result = query_result.filter(
                    models.Q(title__icontains=query_item) |
                    models.Q(content__icontains=query_item))
        return query_result


class SolutionContent(models.Model):
    """
    用于管理解决方案内容
    """
    POSITION_CHOICES = (
        (0, '位置0'),
        (1, '位置1'),
        (2, '位置2'),
        (3, '位置3'),
        (4, '位置4'),
    )
    solution = models.ForeignKey(
        Solution,
        db_column='solution_id',
        help_text='*选择所属解决方案',
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
    objects = SolutionContentManager()

    class Meta:
        db_table = 'portal_solution_content'
        verbose_name_plural = '解决方案内容'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # 保存时自动更新数据修改时间
        self.update = datetime.now()
        return super(SolutionContent, self).save(*args, **kwargs)
