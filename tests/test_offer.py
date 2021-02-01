def test_get_all(all_offers):
    json = all_offers.json()
    assert all_offers.status_code == 200
    assert isinstance(json, list)


def test_get_by_id(api, random_offer):
    random_offer_id = random_offer['id']
    res = api.offer.get(random_offer_id)
    json = res.json()
    assert res.status_code == 200
    assert isinstance(json, dict)
    assert json['id'] == random_offer_id


def test_download_langing(api):
    raise NotImplementedError


def test_get_file_data(api):
    raise NotImplementedError
