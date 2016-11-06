# -*- coding: utf-8 _8-
from django.db import models
from datetime import datetime
from .base import BaseManager


class SlideManager(BaseManager):
    def get_enabled_slide(self):
        """
        获取所有处于有效状态的Slide数据并按更新时间排序
        :return:
        """
        return self.query().filter(enable=1).order_by('-update')


class Slide(models.Model):
    """
    用于管理站点首页幻灯片信息
    """
    ENABLE_CHOICES = (
        (1, '启用'),
        (0, '禁用'),
    )
    title = models.CharField(
        db_column='title',
        max_length=250,
        null=True,
        blank=True,
        help_text='幻灯片主标题,长度限制250个字符',
        verbose_name='标题'
    )
    content = models.TextField(
        db_column='content',
        null=True,
        blank=True,
        help_text='幻灯片内容,可使用HTML代码,区域大小930x250',
        verbose_name='幻灯片内容'
    )
    enable = models.IntegerField(
        db_column='enable',
        default=1,
        choices=ENABLE_CHOICES,
        help_text='*有效状态',
        verbose_name='状态'
    )
    update = models.DateTimeField(
        db_column='update',
        default=datetime.now(),
        editable=False,
        help_text='更新时间',
        verbose_name='更新时间'
    )
    objects = SlideManager()

    class Meta:
        db_table = 'portal_slide'
        verbose_name_plural = '首页幻灯片'

    def __str__(self):
        if self.title is None:
            return ''
        return self.title

    def save(self, *args, **kwargs):
        # 保存时自动更新数据修改时间
        self.update = datetime.now()
        super(Slide, self).save(*args, **kwargs)
