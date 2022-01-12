from rest_framework import mixins, viewsets

from news.models import Article
from news.pagintaion import NewsPageSetPagination
from news.serializers import NewsSerializer


class NewsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Article.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPageSetPagination
