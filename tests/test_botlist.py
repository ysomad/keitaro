def test_get(client):
    resp = client.botlist.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
