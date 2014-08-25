#coding=utf-8
from django.contrib import admin
from portal.models import GlobalSetting, Media, Slide, News, Solution, Product, SP

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

class NewsAdmin(admin.ModelAdmin):
    model = News
    ordering = ['id']
    list_display = ('id', 'title', 'enable', 'update')
    list_filter = ('enable', 'update')

class MediaAdmin(admin.ModelAdmin):
    model = Media
    ordering = ['id']
    list_display = ('id', 'title', 'file', 'update')
    list_filter = ('update', 'title')

class SolutionAdmin(admin.ModelAdmin):
    model = Solution
    ordering = ['id']
    list_display = ('id', 'title', 'keyword', 'enable', 'update')
    list_filter = ('enable', 'update')

class ProductAdmin(admin.ModelAdmin):
    model = Product
    ordering = ['id']
    list_display = ('id', 'title', 'keyword', 'enable', 'update')
    list_filter = ('enable', 'update')

class SPAdmin(admin.ModelAdmin):
    model = SP
    ordering = ['id']
    list_display = ('id', 'solution', 'product')

admin.site.register(GlobalSetting, GlobalSettingAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SP)

