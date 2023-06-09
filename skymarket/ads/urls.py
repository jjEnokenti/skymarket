from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views.ad import AdViewSet
from .views.comment import CommentViewSet


ads_router = SimpleRouter()
ads_router.register('ads', AdViewSet)

comment_router = NestedSimpleRouter(ads_router, 'ads', lookup='ad')
comment_router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(ads_router.urls)),
    path('', include(comment_router.urls)),
]
