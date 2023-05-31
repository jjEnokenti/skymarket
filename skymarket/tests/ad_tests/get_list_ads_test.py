import pytest

from ads.serializers.ad import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_get_list_ads(client):
    ads = AdFactory.create_batch(4)

    response = client.get('/api/ads/')

    expected_response = {
        'count': 4,
        'next': None,
        'previous': None,
        'results': AdListSerializer(ads, many=True).data
    }
    assert response.status_code == 200
    assert response.data['next'] is None
    assert response.data == expected_response
