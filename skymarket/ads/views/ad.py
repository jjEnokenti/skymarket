from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.filters import AdFilter
from ads.models import Ad
from ads.permissions import CanEditOrDelete
from ads.serializers.ad import (
    AdListSerializer,
    AdDetailSerializer,
    CreateAdSerializer,
    UpdateAdSerializer
)


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    default_serializer = AdListSerializer
    serializers = {
        'retrieve': AdDetailSerializer,
        'create': CreateAdSerializer,
        'partial_update': UpdateAdSerializer,
    }

    default_permission = [AllowAny()]
    permissions = {
        'me': [IsAuthenticated()],
        'create': [IsAuthenticated()],
        'retrieve': [IsAuthenticated()],
        'update': [IsAuthenticated(), CanEditOrDelete()],
        'partial_update': [IsAuthenticated(), CanEditOrDelete()],
        'destroy': [IsAuthenticated(), CanEditOrDelete()],
    }

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def perform_create(self, serializer):
        author_id = self.request.user.pk
        serializer.save(author_id=author_id)
