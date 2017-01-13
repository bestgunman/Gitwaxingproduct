from django.contrib import admin
from .models import Brand, Product

class BrandAdmin(admin.ModelAdmin):
	list_display = ['id','name','url','urladdress','content','logo',]

class ProductAdmin(admin.ModelAdmin):
	list_display = ['id','url','title','brand','price','urladdress','content','productimg',]

admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
