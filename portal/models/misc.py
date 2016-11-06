# -*- conding: utf-8 -*-

from django.db import models
from datetime import datetime
from .base import BaseManager


class Media(models.Model):
    """
    UPLOAD_ROOT = 'upload/'
    """
    title = models.CharField(
        db_column='title',
        max_length=250,
        help_text='*媒体文件标题',
        verbose_name='标题'
    )
    '''
    file = models.FileField(
        db_column='file',
        upload_to=UPLOAD_ROOT,
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

    '''
    def save(self, *args, **kwargs):
        #判断文件是否改变
        media_file = str(self.file)
        file_changed = False
        if str(media_file).find(Media.UPLOAD_ROOT) == -1:
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
    '''

    def save(self, *args, **kwargs):
        self.update = datetime.now()
        super(Media, self).save(*args, **kwargs)

    '''
    def delete(self, *args, **kwargs):
        #删除数据记录
        super(Media, self).delete(*args, **kwargs)
        #尝试删除文件
        filename = str(self.file).encode(encoding='utf-8')
        filename = settings.BASE_DIR + filename
        if os.path.exists(filename):
            os.remove(filename)
    '''


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
