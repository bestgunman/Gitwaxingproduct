from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
	url(r'^writeboard/(?P<url>[\w-]+)/$', views.write_board, name="writeboard"),
	url(r'^reviewlist/(?P<product_url>[\w-]+)$', views.review_list, name='review_list'),
]