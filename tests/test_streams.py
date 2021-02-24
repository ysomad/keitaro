import random

from keitaro.utils import generate_random_string


def test_get(client):
    resp = client.streams.get(1)
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == 1


def test_get_deleted(client):
    resp = client.streams.get_deleted()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_search(client):
    resp = client.streams.search('Stream 1')
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['name'] == 'Stream 1'


def test_get_schemas(client):
    resp = client.streams.get_schemas()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    # TODO: add more tests


def test_get_types(client):
    resp = client.streams.get_types()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    # TODO: add more tests


def test_get_actions(client):
    resp = client.streams.get_actions()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    # TODO: add more tests


def test_create(client):
    campaign_id = random.choice(client.campaigns.get().json())['id']
    stream_name = f'Test stream {generate_random_string()}'
    stream_type = random.choice(('regular', 'forced', 'default'))
    action_type = random.choice(client.streams.get_actions().json())['key']
    schema = random.choice(client.streams.get_schemas().json())['value']
    resp = client.streams.create(
        campaign_id=campaign_id, name=stream_name, type=stream_type,
        action_type=action_type, schema=schema)
    data = resp.json()
    assert resp.status_code == 200
    assert data['campaign_id'] == campaign_id
    assert data['schema'] == schema
    assert data['type'] == stream_type
    assert data['name'] == stream_name
    assert data['action_type'] == action_type


def test_disable(client):
    stream = random.choice(client.streams.search('Stream 1').json())
    resp = client.streams.disable(stream['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert data['id'] == stream['id']
    assert data['state'] == 'disabled'


def test_enable(client):
    stream = random.choice(client.streams.search('Stream 1').json())
    disabled_stream = client.streams.disable(stream['id'])
    resp = client.streams.enable(stream['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert data['id'] == stream['id']
    assert data['state'] == 'active'


def test_restore(client):
    deleted_stream = random.choice(client.streams.get_deleted().json())
    resp = client.streams.restore(deleted_stream['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert data['id'] == deleted_stream['id']
    assert data['state'] == 'active'
