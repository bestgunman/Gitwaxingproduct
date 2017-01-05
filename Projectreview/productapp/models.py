from django.db import models
import os

def get_brandimage_path(instance, filename):
	return os.path.join('brand_image', filename)

def get_productimage_path(instance, filename):
	return os.path.join('product_image', filename)

class Brand(models.Model):
	name = models.CharField(max_length = 128)
	content = models.TextField()
	logo = models.ImageField(blank=True, upload_to=get_brandimage_path)

	def __str__(self):
		return self.name

class Product(models.Model):
	title = models.CharField(max_length = 1024)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
	price = models.IntegerField()
	urladdress = models.URLField()
	content = models.TextField()
	productimg = models.ImageField(blank=True, upload_to=get_productimage_path)

	def __str__(self):
		return self.title