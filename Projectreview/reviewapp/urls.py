from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.review_board, name='review_board'),
	url(r'^writeboard/$', views.write_board),
	url(r'^saveboard/$', views.save_board),
]