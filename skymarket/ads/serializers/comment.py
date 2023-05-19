from rest_framework import serializers

from ads.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    """Comments list serializer."""

    pk = serializers.ReadOnlyField(source='id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.ReadOnlyField(source='author.id')
    ad_id = serializers.ReadOnlyField(source='ad.id')
    author_image = serializers.ImageField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        exclude = ('id', 'ad', 'author',)


class CommentCreateSerializer(CommentListSerializer):
    """Comment create serializer."""

    pass


class CommentDetailSerializer(CommentListSerializer):
    """Comment detail serializer."""

    pass


class CommentUpdateSerializer(CommentListSerializer):
    """Comment update serializer."""

    pass
