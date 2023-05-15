from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

routers = SimpleRouter()
routers.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('auth/', include("djoser.urls.jwt")),
]

urlpatterns += routers.urls
