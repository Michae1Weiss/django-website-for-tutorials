from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.web.urls')),
    path('', include('apps.users.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
