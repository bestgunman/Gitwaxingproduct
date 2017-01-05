from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^productdetail/$', views.product_detail),
	url(r'^branddetail/$', views.brand_detail),
]