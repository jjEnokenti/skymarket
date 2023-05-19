from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ads.models import Comment, Ad
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

    def list(self, request, *args, **kwargs):
        self.queryset = Comment.objects.filter(ad=self.kwargs.get('ad_pk'))
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        ad_pk = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_pk)
        serializer.save(author=user, ad=ad)

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)
