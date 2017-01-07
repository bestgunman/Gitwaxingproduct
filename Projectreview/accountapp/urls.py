from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^loginview/$', views.login_view, name='login'),
	url(r'^logoutview/$', views.logout_view, name='logout'),
	url(r'^signupview/$', views.signup_view, name='signup'),
	url(r'^mypageview/$', views.mypage_view, name='mypage'),
	url(r'^userpageview/(?P<username>[\w-]+)/$', views.userpage_view, name='userpage'),
]