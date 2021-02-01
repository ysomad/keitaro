def test_getting_rows_from_botlist(botlist):
    json = botlist.json()
    assert botlist.status_code == 200
    assert isinstance(json, dict)
