from rest_framework.routers import DefaultRouter

from cms_integration.views import ServiceViewSet

router = DefaultRouter()

router.register(r'service', ServiceViewSet, basename='service')

urlpatterns = router.urls
