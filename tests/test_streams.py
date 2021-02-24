def test_get(client):
    resp = client.streams.get(1)
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == 1


def test_get_deleted(client):
    resp = client.streams.get_deleted()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_search(client):
    resp = client.streams.search('Stream 1')
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, list)
    assert data[0]['name'] == 'Stream 1'


def test_get_schemas(client):
    resp = client.streams.get_schemas()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_types(client):
    resp = client.streams.get_types()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_actions(client):
    resp = client.streams.get_actions()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
