# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class News(models.Model):
    """
    用于管理站点新闻消息
    """
    ENABLE_CHOICES = (
        (1, '启用'),
        (0, '禁用'),
    )
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='*新闻标题',
        verbose_name='标题'
    )
    content = models.TextField(
        db_column='content',
        null=True,
        blank=True,
        help_text='*新闻内容',
        verbose_name='内容'
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
        help_text='*有效状态',
        verbose_name='状态'
    )

    class Meta:
        db_table = 'portal_news'
        verbose_name_plural = '新闻'

    def __str__(self):
        return \
            self.title

    def get_update_year(self):
        return \
            self.update.year

    def get_update_day(self):
        return \
            self.update.day

    def save(self, *args, **kwargs):
        # 保存时自动更新数据修改时间
        self.update = datetime.now()
        super(News, self).save(*args, **kwargs)
