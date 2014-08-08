#coding=utf-8
from django.contrib import admin
from portal.models import GlobalSetting, Slide

class GlobalSettingAdmin(admin.ModelAdmin):
    model = GlobalSetting
    ordering = ['key']
    list_display = ('key', 'value', 'update')
    list_filter = ['update']

class SlideAdmin(admin.ModelAdmin):
    model = Slide
    ordering = ['id']
    list_display = ('id', 'title', 'subtitle', 'enable', 'update')
    list_filter = ('enable', 'update')

admin.site.register(GlobalSetting, GlobalSettingAdmin)
admin.site.register(Slide, SlideAdmin)

