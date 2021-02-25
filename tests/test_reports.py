import random


def test_get_labels(client):
    campaign_id = random.choice(client.campaigns.get().json())['id']
    resp = client.reports.get_labels(campaign_id, 'blacklist', 'source')
    assert resp.status_code == 200
    # TODO: more tests


def test_build(client):
    resp = client.reports.build('today', 'Europe/Madrid')
    assert resp.status_code == 200
    # TODO: more tests


def test_update_labels(client):
    campaign_id = random.choice(client.campaigns.get().json())['id']
    resp = client.reports.update_labels(campaign_id, 'ip', {
        'value': {'value': 'blacklist'}
    })
    assert resp.status_code == 200
    # TODO: more tests
