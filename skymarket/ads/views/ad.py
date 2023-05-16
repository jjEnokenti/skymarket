from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.filters import AdFilter
from ads.models import Ad
from ads.permissions import IsOwnerOrStaff, CanEditOrDelete
from ads.serializers.ad import AdSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    default_serializer = AdSerializer
    serializers = {
        'retrieve': AdDetailSerializer,
    }

    default_permission = [AllowAny()]
    permissions = {
        'create': [IsAuthenticated()],
        'retrieve': [IsAuthenticated(), IsOwnerOrStaff()],
        'update': [IsAuthenticated(), CanEditOrDelete()],
        'partial_update': [IsAuthenticated(), CanEditOrDelete()],
        'destroy': [IsAuthenticated(), CanEditOrDelete()],
    }

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)
