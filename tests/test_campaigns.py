from keitaro import Keitaro, Campaign


def test_get():
    client = Keitaro('123123', 'https://example.com')
    campaigns = Campaign(client)
    resp = campaigns.get(1)
    assert resp.status_code == 404
