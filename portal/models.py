#coding=utf-8
__author__ = 'Mervin'
import os
import datetime
from django.conf import settings
from django.db import models
from portal.utils import generate_random_string
from portal.manager import SlideManager, SolutionManager, GlobalSettingManager, ProductManager, SolutionProductManager

class Media(models.Model):
    UPLOAD_ROOT = 'upload/'
    title = models.CharField(max_length=250, help_text='*Title of media')
    file = models.FileField(upload_to=UPLOAD_ROOT)
    update = models.DateTimeField(default=datetime.datetime.now(), editable=False)

    def __unicode__(self):
        return \
            self.title

    def save(self, *args, **kwargs):
        #判断文件是否改变
        file = str(self.file)
        file_changed = False
        if str(file).find(Media.UPLOAD_ROOT) == -1:
            file_changed = True
        if file_changed:
            #查找原数据中的值并尝试删除原文件
            try:
                original_media = Media.objects.get(id=self.id)
                original_file = str(original_media.file).encode(encoding='utf-8')
                original_file = settings.BASE_DIR + original_file
                if os.path.exists(original_file):
                    os.remove(original_file)
            except Exception, error:
                print error
        self.update = datetime.datetime.now()
        super(Media, self).save(*args, **kwargs)
        #更新文件后对生成随机文件名并对文件和数据记录进行修改
        if file_changed:
            try:
                media_item = Media.objects.get(id=self.id)
                original_file = str(media_item.file.file).encode(encoding='utf-8')
                if not os.path.exists(original_file):
                    return
                extend = os.path.splitext(original_file)[1]
                new_name = generate_random_string(16) + extend
                new_file = os.path.join(settings.MEDIA_ROOT, Media.UPLOAD_ROOT, new_name)
                media_item.file = settings.MEDIA_URL + Media.UPLOAD_ROOT + new_name
                os.rename(original_file, new_file)
                super(Media, media_item).save(*args, **kwargs)
            except Exception, error:
                print error


    def delete(self, *args, **kwargs):
        #删除数据记录
        super(Media, self).delete(*args, **kwargs)
        #尝试删除文件
        filename = str(self.file).encode(encoding='utf-8')
        filename = settings.BASE_DIR + filename
        if os.path.exists(filename):
            os.remove(filename)


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
    objects = SlideManager()

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
        ('qq', 'QQ'),
    )
    key = models.CharField(max_length=250, primary_key=True, choices=KEY_CHOICES, help_text='*Key')
    value = models.CharField(max_length=250, null=True, blank=True, help_text='Value')
    update = models.DateTimeField(default=datetime.datetime.now(), editable=False, help_text='Update time')
    objects = GlobalSettingManager()

    def __unicode__(self):
        return \
            self.key

    def save(self, *args, **kwargs):
        self.update = datetime.datetime.now()
        super(GlobalSetting, self).save(*args, **kwargs)

class News(models.Model):
    '''
    用于管理站点新闻消息
    '''
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

class Solution(models.Model):
    '''
    用于管理解决方案信息
    '''
    ENABLE_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    title = models.CharField(max_length=250, help_text='*Title of solution')
    subtitle = models.CharField(max_length=250, null=True, blank=True, help_text='Subtitle')
    enable = models.IntegerField(default=1, choices=ENABLE_CHOICES, help_text='*Enable status')
    image = models.CharField(max_length=250, null=True, blank=True, help_text='Images of solution')
    sketch = models.TextField(null=True, blank=True, help_text='Sketch')
    content = models.TextField(null=True, blank=True, help_text='Content of solution')
    keyword = models.CharField(max_length=250, null=True, blank=True)
    update = models.DateTimeField(default=datetime.datetime.now(), editable=False, help_text='*Update time')
    objects = SolutionManager()

    def __unicode__(self):
        return \
            self.title

    def save(self, *args, **kwargs):
        #保存时自动更新数据修改时间
        self.update = datetime.datetime.now()
        return super(Solution, self).save(*args, **kwargs)

class Product(models.Model):
    '''
    用于管理产品数据
    '''
    ENABLE_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    title = models.CharField(max_length=250, help_text='*Product name')
    subtitle = models.CharField(max_length=250, null=True, blank=True, help_text='Subtitle')
    enable = models.IntegerField(default=1, choices=ENABLE_CHOICES, help_text='*Enable status')
    image = models.CharField(max_length=250, null=True, blank=True, help_text='Images of product')
    sketch = models.TextField(null=True, blank=True, help_text='Sketch')
    content = models.TextField(null=True, blank=True, help_text='Content of solution')
    keyword = models.CharField(max_length=250, null=True, blank=True)
    update = models.DateTimeField(default=datetime.datetime.now(), editable=False, help_text='*Update time')
    solution = models.ForeignKey(Solution, null=True, blank=True)
    objects = ProductManager()

    def __unicode__(self):
        return \
            self.title

    def save(self, *args, **kwargs):
        #保存时自动更新数据修改时间
        self.update = datetime.datetime.now()
        return super(Product, self).save(*args, **kwargs)

class SolutionProduct(models.Model):
    '''
    管理方案和产品的关联
    '''
    solution = models.IntegerField(help_text='solution id')
    product = models.IntegerField(help_text='product id')
    objects = SolutionProductManager()