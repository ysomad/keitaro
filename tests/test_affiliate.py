import random
import json


def test_get_all(keitaro_test_client):
    response = keitaro_test_client.affiliate.get()
    assert response.status_code == 200
    assert isinstance(response, list)


def test_get_by_id(keitaro_test_client, random_affiliate):
    random_affiliate_id = random_affiliate['id']
    response = keitaro_test_client.affiliate.get(random_affiliate_id)
    assert response.status_code == 200
    assert isinstance(response, dict)
    assert response['id'] == random_affiliate_id
