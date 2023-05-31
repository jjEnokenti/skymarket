import pytest


@pytest.fixture()
@pytest.mark.djano_db
def auth_token(client, django_user_model):
    email = 'test@test.ru'
    phone = '+79219879898'
    first_name = 'first'
    last_name = 'last'
    password = '1234'

    django_user_model.objects.create_superuser(
        email=email,
        phone=phone,
        first_name=first_name,
        last_name=last_name,
        password=password,
    )
    response = client.post(
        '/api/token/',
        data={
            'email': email,
            'password': password
        },
        content_type='application/json'
    )

    token = f'Bearer {response.data["access"]}'

    return token
