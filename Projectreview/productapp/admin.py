from django.contrib import admin
from .models import Brand, Product

class BrandAdmin(admin.ModelAdmin):
	list_display = ['name','content','logo',]

class ProductAdmin(admin.ModelAdmin):
	list_display = ['brand','price','urladdress','content','productimg',]

admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
