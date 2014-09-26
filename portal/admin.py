#coding=utf-8
from django.contrib import admin
from portal.models import *


class BaseModelAdmin(admin.ModelAdmin):
    class Media:
        def __init__(self):
            pass

        js = (
            '/static/common/widget/tinymce/tinymce.min.js',
            '/static/common/js/textareas.js',
        )


class GlobalSettingAdmin(BaseModelAdmin):
    model = GlobalSetting
    ordering = ['key']
    list_display = ('key', 'value', 'update')
    list_filter = ['update']


class SlideAdmin(BaseModelAdmin):
    model = Slide
    ordering = ['id']
    list_display = ('id', 'title', 'enable', 'update')
    list_filter = ('enable', 'update')


class NewsAdmin(BaseModelAdmin):
    model = News
    ordering = ['id']
    list_display = ('id', 'title', 'enable', 'update')
    list_filter = ('enable', 'update')


class MediaAdmin(BaseModelAdmin):
    model = Media
    ordering = ['id']
    list_display = ('id', 'title', 'file', 'update')
    list_filter = ('update', 'title')


class PartnerAdmin(BaseModelAdmin):
    model = Partner
    ordering = ['id']
    list_display = ('id', 'title', 'website')


class CustomerAdmin(BaseModelAdmin):
    model = Customer
    ordering = ['id']
    list_display = ('id', 'title', 'fullname')


class SolutionAdmin(BaseModelAdmin):
    model = Solution
    ordering = ['id']
    list_display = ('id', 'title', 'keyword', 'enable', 'update')
    list_filter = ('enable', 'update')


class SolutionContentAdmin(BaseModelAdmin):
    model = SolutionContent
    ordering = ['id']
    list_display = ('id', 'solution', 'title', 'position', 'update')
    list_filter = ('solution', 'update')


class ProductAdmin(BaseModelAdmin):
    model = Product
    ordering = ['id']
    list_display = ('id', 'title', 'keyword', 'enable', 'partner', 'update')
    list_filter = ('enable', 'update')


class ProductContentAdmin(BaseModelAdmin):
    model = ProductContent
    ordering = ['id']
    list_display = ('id', 'product', 'title', 'position', 'update')
    list_filter = ('product', 'update')


class ServiceAdmin(BaseModelAdmin):
    model = Service
    ordering = ['id']
    list_display = ('id', 'title', 'enable', 'update')
    list_filter = ('enable', 'update')


class ProductCustomerAdmin(BaseModelAdmin):
    model = ProductCustomer
    ordering = ['id']
    list_display = ['id', 'product', 'customer']
    list_filter = ['product', 'customer']


class SolutionProductAdmin(BaseModelAdmin):
    model = SolutionProduct
    ordering = ['id']
    list_display = ('id', 'solution', 'product')

admin.site.register(GlobalSetting, GlobalSettingAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(SolutionContent, SolutionContentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductContent, ProductContentAdmin)
admin.site.register(ProductCustomer, ProductCustomerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SolutionProduct, SolutionProductAdmin)