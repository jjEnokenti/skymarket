from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.filters import AdFilter
from ads.models import Ad
from ads.permissions import CanEditOrDeleteAd
from ads.serializers.ad import (
    AdListSerializer,
    AdDetailSerializer,
    AdCreateSerializer,
    AdUpdateSerializer
)


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


@extend_schema_view(
    list=extend_schema(
        tags=['ads'],
        responses=AdListSerializer,
        description='Ads list view',
        summary='ads list'
    ),
    retrieve=extend_schema(
        tags=['ads'],
        responses=AdDetailSerializer,
        description='Ad detail view',
        summary='ad detail'
    ),
    create=extend_schema(
        tags=['ads'],
        responses=AdCreateSerializer,
        description='Ad create view',
        summary='ad create'
    ),
    partial_update=extend_schema(
        tags=['ads'],
        responses=AdUpdateSerializer,
        description='Ad partial update view',
        summary='ad partial update'
    ),
    destroy=extend_schema(
        tags=['ads'],
        description='Ad delete view',
        summary='ad delete'
    ),
)
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    http_method_names = ['get', 'post', 'patch', 'delete']

    default_serializer = AdListSerializer
    serializers = {
        'retrieve': AdDetailSerializer,
        'create': AdCreateSerializer,
        'partial_update': AdUpdateSerializer,
    }

    default_permission = [AllowAny()]
    permissions = {
        'me': [IsAuthenticated()],
        'create': [IsAuthenticated()],
        'retrieve': [IsAuthenticated()],
        'partial_update': [IsAuthenticated(), CanEditOrDeleteAd()],
        'destroy': [IsAuthenticated(), CanEditOrDeleteAd()],
    }

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def perform_create(self, serializer):
        author_id = self.request.user.pk
        serializer.save(author_id=author_id)

    @extend_schema(
        tags=['ads'],
        description='User ads list view',
        summary='user ads list'
    )
    @action(methods=['get'], detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(request, *args, **kwargs)
