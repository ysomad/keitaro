import json
import random


def test_get_all(client):
    resp = client.domains.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_by_id(client):
    random_domain = random.choice(client.domains.get().json())
    resp = client.domains.get(random_domain['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == random_domain['id']
    assert data['name'] == random_domain['name']


def test_get_deleted(client):
    resp = client.domains.get_deleted()
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    for deleted_domain in data:
        assert data[0]['state'] == 'deleted'
