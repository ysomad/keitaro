def test_get_all(all_affiliate):
    json = all_affiliate.json()
    assert all_affiliate.status_code == 200
    assert isinstance(json, list)


def test_get_by_id(api, random_affiliate):
    random_affiliate_id = random_affiliate['id']
    res = api.affiliate.get(random_affiliate_id)
    json = res.json()
    assert res.status_code == 200
    assert isinstance(json, dict)
    assert json['id'] == random_affiliate_id

