from django.contrib import admin
from .models import Comment, Review

class ReviewAdmin(admin.ModelAdmin):
	list_display = ['id','content','author','regdate','score','product','reviewimg',]

class CommentAdmin(admin.ModelAdmin):
	list_display = ['guest','comment','regdate','review',]

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)





	
