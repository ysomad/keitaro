import random

from keitaro.utils import generate_random_string


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


def test_create(client):
    domain_name = f'https://{generate_random_string(16).lower()}.com'
    resp = client.domains.create(
        name=domain_name, default_campaign_id=1, allow_indexing=True)
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['name'] == domain_name
    assert data[0]['default_campaign_id'] == 1
    assert data[0]['allow_indexing'] == True


def test_check(client):
    random_domain = random.choice(client.domains.get().json())
    resp = client.domains.check(random_domain['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['id'] == random_domain['id']
    assert data[0]['name'] == random_domain['name']


def test_restore(client):
    deleted_domain = random.choice(client.domains.get_deleted().json())
    resp = client.domains.restore(deleted_domain['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['id'] == deleted_domain['id']
    assert data[0]['name'] == deleted_domain['name']
    assert data[0]['state'] == 'active'
