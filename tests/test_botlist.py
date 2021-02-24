def test_get(client):
    resp = client.botlist.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)


def test_add(client):
    ips_list = '1.2.3.4\n5.6.7.8\n9.0.1.2\n0.1.2.3'
    resp = client.botlist.add(ips_list)
    data = resp.json()
    botlist_data = client.botlist.get().json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    for ip in ips_list.split('\n'):
        assert ip in botlist_data['value']
