import random

from keitaro.utils import generate_random_string


def test_get_all(client):
    resp = client.landing_pages.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_by_id(client):
    random_landing_page = random.choice(client.landing_pages.get().json())
    resp = client.landing_pages.get(random_landing_page['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == random_landing_page['id']
    assert data['name'] == random_landing_page['name']


def test_get_file(client):
    resp = client.landing_pages.get_file(1, 'assets/landing_page.zip')
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert isinstance(data['data'], str)


def test_get_structure(client):
    random_landing_page = client.landing_pages.get().json()[0]
    resp = client.landing_pages.get_structure(random_landing_page['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert isinstance(data['children'], list)
    # TODO: add more tests


def test_create(client):
    random_string = generate_random_string(6)
    name = f'test LP {random_string}'
    action_type = random.choice(
        ('local_file', 'http', 'curl', 'status404', 'show_text', 'show_html'))
    url = f'https://{random_string}.net'
    resp = client.landing_pages.create(
        name, action_type=action_type, action_payload=url)
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['name'] == name
    assert data['action_payload'] == url
    assert data['action_type'] == action_type


def test_clone(client):
    random_lp = random.choice(client.landing_pages.get().json())
    resp = client.landing_pages.clone(random_lp['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert data['name'] == f'Copy of {random_lp["name"]}'
    assert data['landing_type'] == random_lp['landing_type']
    # TODO: wait until keitaro fixes routing for this method and test again
