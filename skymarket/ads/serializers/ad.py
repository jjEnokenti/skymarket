from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    """Ad list serializer."""

    pk = serializers.IntegerField(source='id')

    class Meta:
        model = Ad
        exclude = ('created_at', 'id', 'author',)


class AdDetailSerializer(AdListSerializer):
    """Ad detail serializer."""

    pk = serializers.IntegerField(source='id', read_only=True)
    phone = serializers.CharField(source='author.phone', read_only=True)
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.IntegerField(source='author.pk', read_only=True)


class AdCreateSerializer(AdDetailSerializer):
    """Ad create serializer."""

    pass


class AdUpdateSerializer(AdCreateSerializer):
    """Ad update serializer."""

    pass
