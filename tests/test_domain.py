import json


def test_get_all(all_domains):
    json = all_domains.json()
    assert all_domains.status_code == 200
    assert isinstance(json, list)


def test_get_by_id(api, random_domain):
    random_domain_id = random_domain['id']
    res = api.domain.get(random_domain_id)
    json = res.json()
    assert res.status_code == 200
    assert isinstance(json, dict)
    assert json['id'] == random_domain_id


def test_get_deleted(all_deleted_domains):
    json = all_deleted_domains.json()
    assert all_deleted_domains.status_code == 200
    assert isinstance(json, list)
