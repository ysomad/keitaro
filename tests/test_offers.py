import random

from keitaro.utils import generate_random_string


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


def test_create(client):
    name = f'Test offer {generate_random_string(6)}'
    payout_value = 12
    payout_currency = 'EUR'
    payout_auto = True
    resp = client.offers.create(
        name, payout_currency=payout_currency, payout_value=payout_value,
        payout_auto=payout_auto)
    data = resp.json()
    assert resp.status_code == 200
    assert data['name'] == name
    assert data['payout_value'] == payout_value
    assert data['payout_auto'] == payout_auto
    assert data['payout_currency'] == payout_currency


def test_clone(client):
    new_offer = client.offers.create(
        f'Test offer {generate_random_string()}').json()
    resp = client.offers.clone(new_offer['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['name'] == f'Copy of {new_offer["name"]}'
    assert int(data[0]['id']) == int(new_offer['id']) + 1
