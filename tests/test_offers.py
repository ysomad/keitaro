import json

from keitaro import api, get_random_id, generate_name


def test_get():
    response = api.offers.get()
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_by_id():
    offer_id = get_random_id(api.offers.get())
    response = api.offers.get(offer_id)
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, dict)
    assert json['id'] == offer_id


def test_create():
    name = generate_name('test_create')
    group_id = 14
    payload = {
        'name': name,
        'group_id': group_id
    }
    response = api.offers.create(payload)
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, dict)
    assert json['name'] == name
    assert json['group_id'] == group_id


def test_delete():
    payload = {
        'name': generate_name('test_delete'),
        'group_id': 14
    }
    created_offer = api.offers.create(payload)
    created_offer_id = created_offer.json()['id']
    response = api.offers.delete(created_offer_id)
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, list)
    assert json[0]['id'] == int(created_offer_id)
    assert json[0]['state'] == 'deleted'


def test_update():
    name = generate_name('test_update')
    offer_payload = {
        'name': name,
        'country': 'GB',
        'action_payload': 'https://example.com'
    }
    offer = api.offers.create(offer_payload).json()

    updated_name = name + '_updated'
    updated_action_payload = 'https://updatedurl.net'
    payload = {
        'name': updated_name,
        'country': 'BH',
        'action_payload': updated_action_payload
    }
    response = api.offers.update(offer['id'], payload)
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, dict)
    assert json['name'] == updated_name
    assert json['country'][0] == 'BH'
    assert json['action_payload'] == updated_action_payload