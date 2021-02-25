import random

from keitaro.utils import generate_random_string


def test_get_all(client):
    resp = client.traffic_sources.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_by_id(client):
    random_traffic_source = random.choice(client.traffic_sources.get().json())
    resp = client.traffic_sources.get(random_traffic_source['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == random_traffic_source['id']
    assert data['name'] == random_traffic_source['name']


def test_create(client):
    name = f'Test AN {generate_random_string()}'
    postback_url = f'https://{name}.com'
    state = 'active'
    traffic_loss = 5
    resp = client.traffic_sources.create(
        name=name, postback_url=postback_url, state=state,
        traffic_loss=traffic_loss)
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['name'] == name
    assert data['postback_url'] == postback_url
    assert data['traffic_loss'] == traffic_loss


def test_clone(client):
    new_source = client.traffic_sources.create(
        f'test clone {generate_random_string()}').json()
    resp = client.traffic_sources.clone(new_source['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['name'] == f'Copy of {new_source["name"]}'
