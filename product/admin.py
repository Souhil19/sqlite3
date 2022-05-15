from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','date_production','made_in','qte','price')


admin.site.register(Product,ProductAdmin)