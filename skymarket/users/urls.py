from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

routers = SimpleRouter()
routers.register('users', UserViewSet, basename='users')

urlpatterns = [
    # path('auth/', include("djoser.urls.jwt")),
]

urlpatterns += routers.urls
