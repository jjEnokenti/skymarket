from rest_framework import serializers

from ads.models import Comment
from users.serializers import CommentUserSerializer


class CommentListSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели

    class Meta:
        model = Comment
        exclude = ('created_at',)


class CommentCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):
    ad = serializers.SlugRelatedField(slug_field='title', read_only=True)
    author = CommentUserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',)
