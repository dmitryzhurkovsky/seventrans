from django.conf import settings
from rest_framework import serializers

from cms_integration.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'title_ru',
            'title_en',
            'img',
            'preview_ru',
            'preview_en',
            'slug'
        )

    def get_language(self):
        return self.context['request'].headers.get('Accept-Language')
