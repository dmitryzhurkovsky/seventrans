from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('api/v1/', include('news.urls')),
    path('api/v1/', include('cms_integration.urls')),
    path('cms_integration/', include('cms_integration.urls')),
]
