import random

from keitaro.utils import generate_random_string


def test_get_all(client):
    resp = client.affiliate_networks.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_by_id(client, random_affiliate_network):
    resp = client.affiliate_networks.get(random_affiliate_network['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == random_affiliate_network['id']
    assert data['name'] == random_affiliate_network['name']


def test_create(client):
    random_string = generate_random_string()
    name = f'Test AN {random_string}'
    postback_url = f'https://{random_string}.com/'
    notes = 'Test notes'
    state = 'active'
    resp = client.affiliate_networks.create(
        name=name, postback_url=postback_url, notes=notes, state=state)
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['name'] == name
    assert data['postback_url'] == postback_url
    assert data['notes'] == notes
    assert data['state'] == state


def test_clone(client):
    name = f'test AN {generate_random_string()}'
    new_affiliate_network = client.affiliate_networks.create(name=name).json()
    resp = client.affiliate_networks.clone(new_affiliate_network['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['name'] == f"Copy of {new_affiliate_network['name']}"


def test_update(client):
    random_aff = random.choice(client.affiliate_networks.get().json())
    random_string = generate_random_string()
    name = f'Updated name {random_string}'
    postback_url = f'https://{random_string}.com'
    resp = client.affiliate_networks.update(
        random_aff['id'], name, postback_url)
    data = resp.json()
    assert resp.status_code == 200
    assert data['id'] == random_aff['id']
    assert data['name'] == name
    assert data['postback_url'] == postback_url
