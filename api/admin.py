from django.contrib import admin
from .models import *
# Register your models here.

@admin.register( User, Institution, Agent)
class ProductAdmin(admin.ModelAdmin):
    # list_display=('id', 'caption', 'author', 'publish_time')
    pass
# admin.site.register(Product, ProductAdmin)