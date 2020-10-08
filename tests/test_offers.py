import random

from keitaro import api, get_random_id, generate_name
from keitaropy.models import Model


def test_get():
    response = api.offers.get()
    assert isinstance(response, list)


def test_get_by_id():
    offer_id = get_random_id()
    response = api.offers.get(offer_id)
    assert isinstance(response, dict)
    assert response['id'] == offer_id


def test_create():
    name = generate_name()
    group_id = 14
    payload = {
        'name': name,
        'group_id': group_id
    }
    response = api.offers.create(payload)
    assert isinstance(response, dict)
    assert response['name'] == name
    assert response['group_id'] == group_id


def test_delete():
    payload = {
        'name': generate_name(),
        'group_id': 14
    }
    created_offer = api.offers.create(payload)
    response = api.offers.delete(created_offer['id'])
    assert isinstance(response, list)
    assert response[0]['id'] == int(created_offer['id'])
    assert response[0]['state'] == 'deleted'


def test_update():
    name = generate_name()
    new_offer_payload = {
        'name': name,
        'country': 'GB',
        'action_payload': 'https://example.com'
    }
    created_offer = api.offers.create(new_offer_payload)

    updated_name = name + '_updated'
    updated_action_payload = 'https://updatedurl.net'
    payload = {
        'name': updated_name,
        'country': 'BH',
        'action_payload': updated_action_payload
    }
    response = api.offers.update(created_offer['id'], payload)
    assert isinstance(response, dict)
    assert response['name'] == updated_name
    assert response['country'][0] == 'BH'
    assert response['action_payload'] == updated_action_payload