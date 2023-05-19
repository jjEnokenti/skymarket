from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Ad
        exclude = ('created_at', 'id', 'author',)


class AdDetailSerializer(AdListSerializer):
    pk = serializers.ReadOnlyField(source='id')
    phone = serializers.CharField(source='author.phone', read_only=True)
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.ReadOnlyField(source='author.pk')


class CreateAdSerializer(AdDetailSerializer):
    pass


class UpdateAdSerializer(CreateAdSerializer):
    pass
