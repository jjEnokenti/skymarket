from rest_framework import serializers

from ads.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source='id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.ReadOnlyField(source='author.id')
    ad_id = serializers.ReadOnlyField(source='ad.id')
    author_image = serializers.ImageField(source='author.image')

    class Meta:
        model = Comment
        exclude = ('id', 'ad', 'author',)


class CommentCreateSerializer(CommentListSerializer):
    pass


class CommentDetailSerializer(CommentListSerializer):
    pass


class CommentUpdateSerializer(CommentListSerializer):
    pass