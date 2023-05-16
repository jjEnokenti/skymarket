from django_filters import rest_framework as filters

from .models import Ad


class AdFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ('title',)
