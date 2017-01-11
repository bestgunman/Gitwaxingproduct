from django.conf.urls import url
from . import views
from reviewapp.views import review_list

urlpatterns = [
	url(r'^productlist/$', views.product_list, name='product_list'),
	url(r'^productdetail/(?P<url>[\w-]+)/$', views.product_detail, name='productdetail'),
	url(r'^brandlist/$', views.brand_list, name='brand_list'),
	url(r'^branddetail/(?P<url>[\w-]+)/$', views.brand_detail, name='branddetail'),
]