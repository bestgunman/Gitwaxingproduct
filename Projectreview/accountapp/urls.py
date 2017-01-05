from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^loginview/$', views.login_view, name='login'),
	url(r'^logoutview/$', views.logout_view, name='logout'),
	url(r'^signupview/$', views.signup_view, name='signup'),
]