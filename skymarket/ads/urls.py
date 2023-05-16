from django.urls import include, path
from rest_framework import routers

from .views.ad import AdViewSet
from .views.comment import CommentViewSet

# TODO настройка роутов для модели

router = routers.SimpleRouter()
router.register('ads', AdViewSet, basename='ads')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [

]

urlpatterns += router.urls
