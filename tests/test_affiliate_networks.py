import random
import json


def test_get_all(client):
    resp = client.affiliate_networks.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_by_id(client):
    all_affiliate_networks = client.affiliate_networks.get().json()
    random_affiliate_network = random.choice(all_affiliate_networks)
    resp = client.affiliate_networks.get(random_affiliate_network['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == random_affiliate_network['id']
    assert data['name'] == random_affiliate_network['name']