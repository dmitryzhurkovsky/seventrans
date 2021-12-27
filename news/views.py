from rest_framework import mixins, viewsets

from news.models import Article


class NewsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Article.objects.all()
