import json


def test_get_all(all_campaigns):
    json = all_campaigns.json()
    assert all_campaigns.status_code == 200
    assert isinstance(json, list)


def test_get_by_id(api, random_campaign):
    random_campaign_id = random_campaign['id']
    res = api.campaign.get(random_campaign_id)
    json = res.json()
    assert res.status_code == 200
    assert isinstance(json, dict)
    assert json['id'] == random_campaign_id


def test_get_deleted(all_deleted_campaigns):
    json == all_deleted_campaigns
    assert all_deleted_campaigns.status_code == 200
    assert isinstance(json, list)
    for campaign in json:
        assert json['state'] == 'deleted'


def test_get_streams():
    # TODO: write tests for getting streams of campaign
    raise NotImplementedError






