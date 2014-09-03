#coding=utf-8
from django.contrib import admin
from portal.models import \
    GlobalSetting, \
    Media, \
    Slide, \
    News, \
    Partner, \
    Customer, \
    Solution, \
    SolutionContent, \
    Product, \
    ProductContent, \
    ProductCustomer, \
    SolutionProduct


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


class PartnerAdmin(admin.ModelAdmin):
    model = Partner
    ordering = ['id']
    list_display = ('id', 'title', 'website')


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    ordering = ['id']
    list_display = ('id', 'title', 'fullname')


class SolutionAdmin(admin.ModelAdmin):
    model = Solution
    ordering = ['id']
    list_display = ('id', 'title', 'keyword', 'enable', 'update')
    list_filter = ('enable', 'update')


class SolutionContentAdmin(admin.ModelAdmin):
    model = SolutionContent
    ordering = ['id']
    list_display = ('id', 'solution', 'title', 'position', 'update')
    list_filter = ('solution', 'update')


class ProductAdmin(admin.ModelAdmin):
    model = Product
    ordering = ['id']
    list_display = ('id', 'title', 'keyword', 'enable', 'partner', 'update')
    list_filter = ('enable', 'update')


class ProductContentAdmin(admin.ModelAdmin):
    model = ProductContent
    ordering = ['id']
    list_display = ('id', 'product', 'title', 'position', 'update')
    list_filter = ('product', 'update')


class ProductCustomerAdmin(admin.ModelAdmin):
    model = ProductCustomer
    ordering = ['id']
    list_display = ['id', 'product', 'customer']
    list_filter = ['product', 'customer']

class SolutionProductAdmin(admin.ModelAdmin):
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
admin.site.register(SolutionProduct, SolutionProductAdmin)