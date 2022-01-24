from rest_framework import serializers

from news.models import Article


class NewsSerializer(serializers.ModelSerializer):
    publish_date = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'publish_date',
            'body',
            'preview_body',
            'img_url',
        )

    def get_publish_date(self, obj):
        return obj.publish_date.strftime('%d.%m.%Y')
