from rest_framework import serializers

from news.models import Article


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'title',
            'publish_date',
            'body',
            'preview_body',
            'img_url',
        )