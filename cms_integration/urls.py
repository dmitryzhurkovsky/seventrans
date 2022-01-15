from rest_framework.routers import DefaultRouter

from cms_integration.views import ServiceViewSet

router = DefaultRouter()

router.register(r'services', ServiceViewSet, basename='services')

urlpatterns = router.urls
