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
