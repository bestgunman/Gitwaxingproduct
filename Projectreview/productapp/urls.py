from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^productdetail/(?P<url>[\w-]+)/$', views.product_detail, name='productdetail'),
	url(r'^branddetail/$', views.brand_detail),
]