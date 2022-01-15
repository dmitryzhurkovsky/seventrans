from rest_framework import serializers

from cms_integration.models import Service


class ServiceSerializer(serializers.Serializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = (
            'title_en',
            'title_ru',
            'img',
            'content_en',
            'content_ru',
        )

    def get_content(self, instance):
        language = self.context['request'].headers.get('Accept-Language')

        if language == 'ru':
            return instance.content_ru

        return instance.content_en
