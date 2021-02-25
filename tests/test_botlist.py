from keitaro.utils import string_to_list


def test_get(client):
    resp = client.botlist.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)


def test_add(client):
    ip_list = ['1.2.3.4', '5.6.7.8', '9.0.1.2', '0.1.2.3']
    resp = client.botlist.add(ip_list)
    data = resp.json()
    botlist_data = string_to_list(client.botlist.get().json()['value'])
    assert resp.status_code == 200
    assert isinstance(data, dict)
    for ip in ip_list:
        assert ip in botlist_data


def test_update(client):
    ip_list = ['1.3.3.7', '1.4.8.8']
    resp = client.botlist.update(ip_list)
    data = resp.json()
    botlist_data = client.botlist.get().json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert isinstance(data['count'], int)
    assert data['count'] == len(ip_list)
