from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^loginview/$', views.login_view),
	url(r'^logoutview/$', views.logout_view),
	url(r'^signupview/$', views.signup_view),
]