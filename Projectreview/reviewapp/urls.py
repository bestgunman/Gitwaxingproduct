from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.review_board, name='review_board'),
	url(r'^(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
	url(r'^writeboard/(?P<url>[\w-]+)/$', views.write_board, name="writeboard"),
]