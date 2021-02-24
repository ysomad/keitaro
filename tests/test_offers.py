import json
import random


def test_get_all(client):
    resp = client.offers.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_by_id(client):
    random_offer = random.choice(client.offers.get().json())
    resp = client.offers.get(random_offer['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == random_offer['id']
    assert data['name'] == random_offer['name']
