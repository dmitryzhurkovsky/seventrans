from rest_framework import serializers


class ServiceSerializer(serializers.Serializer):
    content = serializers.SerializerMethodField()

    def get_content(self, instance):
        language = self.context['request'].headers.get('Accept-Language')

        if language == 'ru':
            return instance.content_ru

        return instance.content_en