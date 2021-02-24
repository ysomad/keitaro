def test_clean_stats(client):
    start_date = '2021-04-01 10:10'
    end_date = '2021-01-12 10:10'
    resp = client.clicks.clean_stats(
        start_date=start_date, end_date=end_date)
    assert resp.status_code == 200
    assert isinstance(resp.json()['success'], bool)
    assert resp.json()['success'] == True


def test_get_log(client):
    resp = client.clicks.get_log(log_range=2)
    assert resp.status_code == 200
    # TODO: add more tests
