from rest_framework.routers import DefaultRouter

from news.views import NewsViewSet

router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')

urlpatterns = router.urls
