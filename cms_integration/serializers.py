from rest_framework import serializers

from cms_integration.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = (
            'id',
            'title',
            'img',
            'content',
        )

    def get_language(self):
        return self.context['request'].headers.get('Accept-Language')

    def get_content(self, instance):
        language = self.get_language()

        if language == 'ru':
            return instance.content_1_ru

        return instance.content_1_en

    def get_title(self, instance):
        language = self.get_language()

        if language == 'ru':
            return instance.title_ru

        return instance.title_en