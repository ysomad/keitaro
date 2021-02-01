def test_get_all(keitaro_test_client):
    response = keitaro_test_client.campaign.get()
    assert response.status_code == 200
    assert isinstance(response, list)


def test_get_by_id(keitaro_test_client, random_campaign):
    random_campaign_id = random_campaign['id']
    response = keitaro_test_client.campaign.get(random_campaign_id)
    assert response.status_code == 200
    assert isinstance(response, dict)
    assert response['id'] == random_campaign_id


def test_get_deleted(keitaro_test_client):
    response = keitaro_test_client.campaign.get_deleted()
    assert response.status_code == 200
    assert isinstance(response, list)
    for campaign in response:
        assert campaign['state'] == 'deleted'
