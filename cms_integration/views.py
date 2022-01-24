from rest_framework import mixins, viewsets

from cms_integration.models import Service
from cms_integration.pagintaion import ServicePageSetPagination
from cms_integration.serializers import ServiceSerializer


class ServiceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    pagination_class = ServicePageSetPagination
