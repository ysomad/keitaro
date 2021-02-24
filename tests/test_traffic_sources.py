import random


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
