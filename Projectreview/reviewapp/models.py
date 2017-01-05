from django.db import models
from django.contrib.auth.models import User
from productapp.models import Product
import os, datetime

def get_image_path(instance, filename):
	return os.path.join('review_image', filename)

class Review(models.Model):
	title = models.CharField(max_length = 1024)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	regdate = models.DateTimeField(auto_now_add = True)
	score = models.IntegerField()
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	reviewimg = models.ImageField(blank=True, upload_to=get_image_path)

	def __str__(self):
		return self.title
	class Meta:
		ordering = ('title',)

class Comment(models.Model):
	guest = models.ForeignKey(User, on_delete = models.CASCADE)
	comment = models.CharField(max_length = 2048)
	regdate = models.DateTimeField(auto_now_add = True)
	review = models.ForeignKey(Review, on_delete = models.CASCADE)

	def __str__(self):
		return self.comment