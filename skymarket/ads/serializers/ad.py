from rest_framework import serializers

from ads.models import Ad
from users.serializers import AdUserSerializer


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели

    class Meta:
        model = Ad
        exclude = ('created_at',)


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author = AdUserSerializer()

    class Meta:
        model = Ad
        fields = '__all__'
