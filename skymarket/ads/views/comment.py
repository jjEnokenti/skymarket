from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ads.models import Comment
from ads.permissions import CanEditOrDelete
from ads.serializers.comment import (
    CommentListSerializer,
    CommentDetailSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer
)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    default_serializer = CommentListSerializer
    serializers = {
        'retrieve': CommentDetailSerializer,
        'create': CommentCreateSerializer,
        'update': CommentUpdateSerializer,
        'partial_update': CommentUpdateSerializer,
    }

    default_permission = [IsAuthenticated()]
    permissions = {
        'update': [IsAuthenticated(), CanEditOrDelete()],
        'partial_update': [IsAuthenticated(), CanEditOrDelete()],
        'destroy': [IsAuthenticated(), CanEditOrDelete()]
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)
