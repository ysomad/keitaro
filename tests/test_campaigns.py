import json
import random

from keitaro.utils import generate_random_string


def test_get_all(client):
    resp = client.campaigns.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_by_id(client):
    all_campaigns = client.campaigns.get().json()
    random_campaign = random.choice(all_campaigns)
    resp = client.campaigns.get(random_campaign['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == random_campaign['id']
    assert data['name'] == random_campaign['name']


def test_get_deleted(client):
    resp = client.campaigns.get_deleted()
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    for campaign in data:
        assert data[0]['state'] == 'deleted'


def test_get_streams(client):
    first_campaign = client.campaigns.get(1).json()
    resp = client.campaigns.get_streams(1)
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['campaign_id'] == first_campaign['id']
    # TODO: check this test


def test_create(client):
    name = f'test campaign {generate_random_string()}'
    cost_currency = 'RUB'
    campaign_type = 'position'
    resp = client.campaigns.create(
        name=name, cost_currency=cost_currency, type=campaign_type)
    data = resp.json()
    assert resp.status_code == 200
    isinstance(data, dict)
    assert data['name'] == name
    assert data['type'] == campaign_type
    assert data['cost_currency'] == cost_currency


def test_get_by_name(client):
    name = f'test campaign {generate_random_string()}'
    resp = client.campaigns.create(name=name)
    data = resp.json()
    filtered_campaigns = client.campaigns.get_by_name(name)
    assert resp.status_code == 200
    assert isinstance(filtered_campaigns, list)
    assert filtered_campaigns[0]['name'] == data['name']


def test_disable(client):
    campaign_name = f'test campaign {generate_random_string()}'
    campaign = client.campaigns.create(
        name=campaign_name, state='active').json()
    resp = client.campaigns.disable(1)
    data = resp.json()[0]
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['state'] == 'disabled'
