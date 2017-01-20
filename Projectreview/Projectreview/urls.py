from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from productapp.views import product_list
from reviewapp.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^review/', include('reviewapp.urls')),
    url(r'^product/', include('productapp.urls')),
    url(r'^account/', include('accountapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )