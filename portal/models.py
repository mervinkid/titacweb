#coding=utf-8
__author__ = 'Mervin'
import os
import datetime
from django.conf import settings
from django.db import models
from portal.utils import generate_random_string
from portal.manager import SlideManager, SolutionManager, GlobalSettingManager, ProductManager, SPManager

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
    subtitle = models.CharField(
        db_column='subtitle',
        max_length=250,
        null=True,
        blank=True,
        help_text='幻灯片副标题，显示在主标题之下,长度限制250个字符',
        verbose_name='副标题'
    )
    heading = models.CharField(
        db_column='heading',
        max_length=250,
        null=True,
        blank=True,
        help_text='显示在内容上部,长度限制250个字符',
        verbose_name='加粗文本'
    )
    content = models.TextField(
        db_column='content',
        null=True,
        blank=True,
        help_text='幻灯片内容,可使用HTML代码',
        verbose_name='幻灯片内容'
    )
    note = models.TextField(
        db_column='note',
        null=True,
        blank=True,
        help_text='幻灯片注解,先是在内容最下部',
        verbose_name='幻灯片注解'
    )
    image = models.TextField(
        db_column='image',
        null=True,
        blank=True,
        help_text='配图地址,可使用base64数据',
        verbose_name='配图地址'
    )
    link = models.TextField(
        db_column='link',
        null=True,
        blank=True,
        default='/',
        help_text='链接地址',
        verbose_name='链接地址'
    )
    link_text = models.CharField(
        db_column='link_text',
        max_length=250,
        null=True,
        blank=True,
        help_text='链接上显示的文本',
        verbose_name='链接文本'
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
        default=datetime.datetime.now(),
        editable=False,
        help_text='更新时间',
        verbose_name='更新时间'
    )
    objects = SlideManager()

    class Meta:
        db_table = 'portal_slide'
        verbose_name_plural = '首页幻灯片'

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
        ('keyword', '页面Keyword'),
        ('description', '页面Description'),
        ('call', '联系电话'),
        ('mail', '联系邮箱'),
        ('qq', '联系QQ'),
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
        default=datetime.datetime.now(),
        editable=False,
        help_text='*更新时间',
        verbose_name='更新时间'
    )
    objects = GlobalSettingManager()

    class Meta:
        db_table = 'portal_global_setting'
        verbose_name_plural = '全局配置'

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
        default=datetime.datetime.now(),
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
    image = models.CharField(
        db_column='image',
        max_length=250,
        null=True,
        blank=True,
        help_text='支持base64数据',
        verbose_name='配图地址'
    )
    sketch = models.TextField(
        db_column='sketch',
        null=True,
        blank=True,
        help_text='显示在标题下',
        verbose_name='简介'
    )
    content = models.TextField(
        db_column='content',
        null=True,
        blank=True,
        help_text='解决方案内容,支持HTML代码',
        verbose_name='内容'
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
        default=datetime.datetime.now(),
        editable=False, help_text='*更新时间',
        verbose_name='更新时间'
    )
    objects = SolutionManager()

    class Meta:
        db_table = 'portal_solution'
        verbose_name_plural = '解决方案'

    def __unicode__(self):
        return \
            self.title

    def save(self, *args, **kwargs):
        #保存时自动更新数据修改时间
        self.update = datetime.datetime.now()
        return super(Solution, self).save(*args, **kwargs)

class SolutionContent(models.Model):
    '''
    用于管理解决方案内容
    '''
    solution = models.ForeignKey(
        Solution,
        db_column='solution_id',
        help_text='*选择所属解决方案',
        verbose_name='解决方案'
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

    class Meta:
        db_table = 'portal_solution_content'
        verbose_name_plural = '解决方案内容'

    def __unicode__(self):
            return self.title

class Product(models.Model):
    '''
    用于管理产品数据
    '''
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
    image = models.CharField(
        db_column='image',
        max_length=250,
        null=True,
        blank=True,
        help_text='配图地址,支持base64数据',
        verbose_name='配图地址'
    )
    sketch = models.TextField(
        db_column='sketch',
        null=True,
        blank=True,
        help_text='显示在标题之下',
        verbose_name='简介'
    )
    content = models.TextField(
        db_column='content',
        null=True,
        blank=True,
        help_text='支持HTML代码',
        verbose_name='内容'
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
        default=datetime.datetime.now(),
        editable=False,
        help_text='*更新时间',
        verbose_name='更新时间'
    )
    objects = ProductManager()

    class Meta:
        db_table = 'portal_product'
        verbose_name_plural = '产品'

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
    solution = models.ForeignKey(
        Solution,
        db_column='solution_id',
        help_text='*选择解决方案',
        verbose_name='解决方案'
    )
    product = models.ForeignKey(
        Product,
        db_column='product_id',
        help_text='*选择产品',
        verbose_name='产品'
    )
    objects = SPManager()

    class Meta:
        db_table = 'portal_solution_product'
        verbose_name_plural = '解决方案与产品关联'