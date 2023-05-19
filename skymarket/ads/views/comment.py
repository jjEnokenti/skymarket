from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ads.models import Comment, Ad
from ads.permissions import CanEditOrDeleteComment
from ads.serializers.comment import (
    CommentListSerializer,
    CommentDetailSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer
)


@extend_schema_view(
    list=extend_schema(
        tags=['comments'],
        responses=CommentListSerializer,
        description='Comments list view',
        summary='comments list'
    ),
    retrieve=extend_schema(
        tags=['comments'],
        responses=CommentDetailSerializer,
        description='Comment detail view',
        summary='comment detail'
    ),
    create=extend_schema(
        tags=['comments'],
        responses=CommentCreateSerializer,
        description='Comment create view',
        summary='comment create'
    ),
    partial_update=extend_schema(
        tags=['comments'],
        responses=CommentUpdateSerializer,
        description='Comment partial update view',
        summary='Comment partial update'
    ),
    destroy=extend_schema(
        tags=['comments'],
        description='Comment delete view',
        summary='comment delete'
    ),
)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    default_serializer = CommentListSerializer
    serializers = {
        'retrieve': CommentDetailSerializer,
        'create': CommentCreateSerializer,
        'partial_update': CommentUpdateSerializer,
    }

    default_permission = [IsAuthenticated()]
    permissions = {
        'partial_update': [IsAuthenticated(), CanEditOrDeleteComment()],
        'destroy': [IsAuthenticated(), CanEditOrDeleteComment()]
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_queryset(self):
        if self.action in ['retrieve', 'partial_update', 'destroy']:
            return Comment.objects.filter(
                ad=self.kwargs.get('ad_pk'),
                pk=self.kwargs.get('pk')
            )
        elif self.action == 'list':
            return Comment.objects.filter(
                ad=self.kwargs.get('ad_pk')
            )

    def perform_create(self, serializer):
        user = self.request.user
        ad_pk = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_pk)
        serializer.save(author=user, ad=ad)
