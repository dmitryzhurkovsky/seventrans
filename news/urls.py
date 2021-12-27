from rest_framework.routers import DefaultRouter

from news.models import Article

router = DefaultRouter()

router.register(r'news', Article, basename='news')

urls = router.urls
