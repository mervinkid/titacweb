from django.contrib import admin
from portal.models import Slide

class SlideAdmin(admin.ModelAdmin):
    model = Slide
    ordering = ['id']
    list_display = ('id', 'title', 'subtitle', 'enable', 'update')
    list_filter = ('enable', 'update')

admin.site.register(Slide, SlideAdmin)
