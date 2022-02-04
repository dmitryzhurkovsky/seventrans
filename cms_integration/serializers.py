from django.conf import settings
from rest_framework import serializers

from cms_integration.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = (
            'id',
            'title',
            'img',
            'preview_ru',
            'preview_en',
            'slug'
        )

    def get_language(self):
        return self.context['request'].headers.get('Accept-Language')

    def get_title(self, instance):
        language = self.get_language()

        if language == 'ru':
            return instance.title_ru

        return instance.title_en
