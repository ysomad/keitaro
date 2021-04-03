from keitaro.utils import generate_random_string


def test_get(client):
    resp = client.users.get(1)
    assert resp.status_code == 200
    assert resp.json()['id'] == 1


def test_create(client):
    random_string = generate_random_string()
    login = f'TestUser{random_string}'
    password = random_string
    user_type = 'ADMIN'
    resp = client.users.create(login, password, user_type)
    data = resp.json()
    assert resp.status_code == 200
    assert data['login'] == login
    assert data['type'] == user_type
