import random

from keitaro.utils import generate_random_string


def test_get(client):
    random_group_type = random.choice(('campaigns', 'offers', 'landings'))
    resp = client.groups.get(random_group_type)
    assert resp.status_code == 200
    assert resp.json()[0]['type'] == random_group_type


def test_create(client):
    group_type = random.choice(('campaigns', 'offers', 'landings'))
    name = f'Group {group_type} {generate_random_string(4)}'
    resp = client.groups.create(name=name, group_type=group_type)
    data = resp.json()
    assert resp.status_code == 200
    assert data['name'] == name
    assert data['type'] == group_type


def test_update(client):
    name = f'Campaign GRP {generate_random_string()}'
    group_to_update = client.groups.create(name, 'campaigns').json()
    new_name = 'Updated ' + name
    resp = client.groups.update(
        group_to_update['id'], new_name)
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == group_to_update['id']
    # TODO: tests again after keitaro fix Update Group method
