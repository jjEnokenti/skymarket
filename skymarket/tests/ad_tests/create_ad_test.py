import pytest


@pytest.mark.django_db
def test_create_ad(client, ad, auth_token):
    data = {
        'title': ad.title,
        'price': ad.price,
        'created_at': ad.created_at,
        'author': ad.author.pk
    }

    response = client.post(
        '/api/ads/',
        data=data,
        HTTP_AUTHORIZATION=auth_token,
        content_type='application/json'
    )

    expected_response = {
        'pk': response.data['pk'],
        'phone': '+79219879898',
        'author_first_name': 'first',
        'author_last_name': 'last',
        'author_id': response.data['author_id'],
        'title': 'test name',
        'price': 1000,
        'description': None,
        'image': None
    }

    assert response.status_code == 201
    assert response.data == expected_response
