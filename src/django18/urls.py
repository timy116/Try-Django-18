from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django18 import views

urlpatterns = [
    url(r'^newsletter/', include('newsletter.urls', namespace='newsletter')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'about/', views.index, name='about'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
