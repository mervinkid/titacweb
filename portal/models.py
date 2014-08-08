#coding=utf-8
from django.db import models
import datetime

class Slide(models.Model):
    '''
    用于管理站点首页幻灯片信息
    '''
    ENABLE_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    title = models.CharField(max_length=250, null=True, blank=True, help_text='Slide main title')
    subtitle = models.CharField(max_length=250, null=True, blank=True, help_text='Slide subtitle')
    heading = models.CharField(max_length=250, null=True, blank=True, help_text='Border text in slide')
    content = models.TextField(null=True, blank=True, help_text='Slide content')
    note = models.TextField(null=True, blank=True, max_length='Slide notes')
    image = models.TextField(null=True, blank=True, default='data:image/gif;base64,R0lGODlhAQAcALMAAMXh96HR97XZ98Hf98Xg97DX97nb98Lf97vc98Tg973d96rU97ba97%2Fe96XS9wAAACH5BAAAAAAALAAAAAABABwAAAQVMLhVBDNItXESAURyDI2CGIxQLE4EADs%3D', help_text='Image source url')
    link = models.TextField(null=True, blank=True, default='/', help_text='Link address')
    button = models.CharField(max_length=250, null=True, blank=True, help_text='Button text')
    enable = models.IntegerField(default=1, choices=ENABLE_CHOICES, help_text='*Enable status')
    update = models.DateTimeField(default=datetime.datetime.now(), editable=False, help_text='Update time')

    def __unicode__(self):
        if self.title is None:
            return u''
        return self.title

    def save(self, *args, **kwargs):
        #保存时自动更新数据修改时间
        self.update = datetime.datetime.now()
        super(Slide, self).save(*args, **kwargs)

class GlobalSetting(models.Model):
    '''
    用于管理站点通用设置
    key:键
    value:值
    '''
    KEY_CHOICES = (
        ('keyword', 'Keyword'),
        ('description', 'Description'),
        ('call', 'Call'),
        ('mail', 'Mail'),
    )
    key = models.CharField(max_length=250, primary_key=True, choices=KEY_CHOICES, help_text='*Key')
    value = models.CharField(max_length=250, null=True, blank=True, help_text='Value')
    update = models.DateTimeField(default=datetime.datetime.now(), editable=False, help_text='Update time')

    def __unicode__(self):
        return \
            self.key

    def save(self, *args, **kwargs):
        self.update = datetime.datetime.now()
        super(GlobalSetting, self).save(*args, **kwargs)

class News(models.Model):
    ENABLE_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    title = models.CharField(max_length=250, help_text='*News title')
    content = models.TextField(help_text='*News content')
    update = models.DateTimeField(default=datetime.datetime.now(), editable=False, help_text='Update time')
    enable = models.IntegerField(default=1, choices=ENABLE_CHOICES, help_text='*News enable status')

    def __unicode__(self):
        return \
            self.title

    def get_update_year(self):
        return \
            self.update.year

    def get_update_day(self):
        return \
            self.update.day

    def save(self, *args, **kwargs):
        #保存时自动更新数据修改时间
        self.update = datetime.datetime.now()
        super(News, self).save(*args, **kwargs)