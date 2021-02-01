def test_get_all(keitaro_test_client):
    response = keitaro_test_client.offer.get()
    assert response.status_code == 200
    assert isinstance(response, list)


def test_get_by_id(keitaro_test_client, random_offer):
    random_offer_id = random_offer['id']
    response = keitaro_test_client.offer.get(random_offer_id)
    assert response.status_code == 200
    assert isinstance(response, dict)
    assert response['id'] == random_offer_id


def test_download_langing(keitaro_test_client, random_offer):
    random_offer_id = random_offer['id']
    response = keitaro_test_client.offer.download(random_offer_id)
    assert response.status_code == 200
    assert isinstance(response, dict)
    # TODO: Add more tests


def test_get_file_data(keitaro_test_client, random_offer):
    random_offer_id = random_offer['id']
    response = keitaro_test_client.offer.file_data(random_offer_id,
            file_path='file.txt')
    assert response.status_code == 20
    assert isinstance(response, dict)
    raise NotImplementedError
