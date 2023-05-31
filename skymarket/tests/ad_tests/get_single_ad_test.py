import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_get_single_ad(client, auth_token):
    ad = AdFactory.create()

    response = client.get(
        f'/api/ads/{ad.pk}/',
        HTTP_AUTHORIZATION=auth_token
    )

    expected_response = {
        "pk": ad.pk,
        "phone": '+79999999999',
        "author_first_name": 'test first name',
        "author_last_name": "test last name",
        "author_id": ad.author.pk,
        "title": "test name",
        "price": 1000,
        "description": None,
        "image": None
    }
    # expected_response = AdDetailSerializer(ad).data

    assert response.status_code == 200
    assert response.data == expected_response
