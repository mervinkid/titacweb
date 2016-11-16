# -*- conding: utf-8 -*-

import os
import re
from datetime import datetime

from django.db import models
from qiniu import Auth, put_file

from portal.utils import generate_string
from titacweb import settings
from .base import BaseManager


class Media(models.Model):
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='*媒体文件标题',
        verbose_name='标题'
    )
    file = models.FileField(
        db_column='file',
        upload_to='upload/',
        help_text='选择本地文件',
        verbose_name='文件'
    )
    '''
    file = models.CharField(
        db_column='file',
        max_length=250,
        help_text='媒体文件URL',
        verbose_name='文件'
    )
    '''
    update = models.DateTimeField(
        db_column='update',
        default=datetime.now(),
        editable=False,
        help_text='*更新时间',
        verbose_name='更新时间'
    )

    class Meta:
        db_table = 'portal_media'
        verbose_name_plural = '媒体文件'

    def __str__(self):
        return \
            self.title

    def save(self, *args, **kwargs):
        file = str(self.file)
        if re.match(r'((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.'
                    r'[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\#\&%_\./-~-]*)?',
                    file, re.I) is not None:
            super(Media, self).save()
            return
        if len(file.split('.')) < 2:
            return
        super(Media, self).save()
        file_type = file.split('.')[-1]
        q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
        bucket_name = settings.QINIU_BUCKET
        # upload new file
        key = '%s.%s' % (generate_string(16), file_type)
        token = q.upload_token(bucket_name, key, 3600)
        ret, info = put_file(token, key, os.path.join(settings.MEDIA_ROOT, 'upload', file.strip().replace(' ', '_')))
        os.remove(os.path.join(settings.MEDIA_ROOT, 'upload', file.strip().replace(' ', '_')))
        print('re: %s' % ret)
        print('info: %s' % info)
        self.file = '%s/%s' % (settings.QINIU_BASE_URL, key)
        super(Media, self).save()


class GlobalSettingManager(BaseManager):
    def get_settings(self):
        """
        获取所有设置信息并将结果以字典形式返回
        :return:
        """
        setting_list = self.query().all()
        settings = {}
        for setting_item in setting_list:
            settings[setting_item.key] = setting_item.value
        return settings

    def get_phone_setting(self):
        """
        获取电话设置信息
        :return:
        """
        try:
            return self.query().get(key='call').value
        except Exception as e:
            print((str(e)))
            return None

    def get_mail_setting(self):
        """
        获取邮箱设置信息
        :return:
        """
        try:
            return self.query().get(key='mail').value
        except Exception as e:
            print((str(e)))
            return None

    def get_keyword_setting(self):
        """
        获取页面Keyword设置信息
        :return:
        """
        try:
            return self.query().get(key='keyword').value
        except Exception as e:
            print((str(e)))
            return str()

    def get_description_setting(self):
        """
        获取页面Description设置信息
        :return:
        """
        try:
            return self.query().get(key='description').value
        except Exception as e:
            print((str(e)))
            return str()


class GlobalSetting(models.Model):
    """
    用于管理站点通用设置
    key:键
    value:值
    """
    KEY_CHOICES = (
        ('keyword', '页面Keyword'),
        ('description', '页面Description'),
        ('call', '联系电话'),
        ('mail', '联系邮箱'),
    )
    key = models.CharField(
        db_column='key',
        max_length=16,
        primary_key=True,
        choices=KEY_CHOICES,
        help_text='*配置项',
        verbose_name='配置项'
    )
    value = models.CharField(
        db_column='value',
        max_length=250,
        null=True,
        blank=True,
        help_text='配置值',
        verbose_name='配置值'
    )
    update = models.DateTimeField(
        db_column='update',
        default=datetime.now(),
        editable=False,
        help_text='*更新时间',
        verbose_name='更新时间'
    )
    objects = GlobalSettingManager()

    class Meta:
        db_table = 'portal_global_setting'
        verbose_name_plural = '全局配置'

    def __str__(self):
        return \
            self.key

    def save(self, *args, **kwargs):
        self.update = datetime.now()
        super(GlobalSetting, self).save(*args, **kwargs)
