from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('api/v1/', include('news.urls')),
    path('cms_integration/', include('cms_integration.urls')),
]

# urlpatterns = i18n_patterns(path(r'^i18n/', include('django.conf.urls.i18n')))
