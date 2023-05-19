from rest_framework import serializers

from ads.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source='id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    ad_id = serializers.ReadOnlyField(source='ad.id')
    author_image = serializers.ImageField(source='author.image')

    class Meta:
        model = Comment
        exclude = ('id', 'ad', 'author',)


class CommentCreateSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source='id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    ad_id = serializers.ReadOnlyField(source='ad.id')

    class Meta:
        model = Comment
        exclude = ('id', 'ad', 'author', 'created_at',)


class CommentDetailSerializer(CommentListSerializer):
    pass


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',)
