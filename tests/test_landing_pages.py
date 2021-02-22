import json
import random


def test_get_all(client):
    resp = client.landing_pages.get()
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_by_id(client):
    random_landing_page = random.choice(client.landing_pages.get().json())
    resp = client.landing_pages.get(random_landing_page['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert data['id'] == random_landing_page['id']
    assert data['name'] == random_landing_page['name']


def test_download(client):
    random_landing_page = random.choice(client.landing_pages.get().json())
    resp = client.landing_pages.download(random_landing_page['id'])
    content_disposition = resp.headers['content-disposition']
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/octet-stream'
    # TODO: add tests for downloading data
    # TODO: add functionality to download data
    raise NotImplementedError


def test_get_file(client):
    resp = client.landing_pages.get_file(1, 'assets/landing_page.zip')
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert isinstance(data['data'], str)


def test_get_structure(client):
    random_landing_page = random.choice(client.landing_pages.get().json())
    resp = client.landing_pages.get_structure(random_landing_page['id'])
    data = resp.json()
    assert resp.status_code == 200
    assert isinstance(data, dict)
    assert isinstance(data['children'], list)
    # TODO: add more tests
    raise NotImplementedError
