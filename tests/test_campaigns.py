import json
import random


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
    random_campaign = random.choice(client.campaigns.get().json())
    resp = client.campaigns.get_streams(random_campaign['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list) 
    assert data[0]['campaign_id'] == random_campaign['id']





