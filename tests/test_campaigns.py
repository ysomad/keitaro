from keitaro import api, get_random_id, generate_name


def test_get():
    response = api.campaigns.get()
    assert isinstance(response, list)


def test_get_by_id():
    campaign_id = get_random_id(api.campaigns.get())
    response = api.campaigns.get(campaign_id)
    assert isinstance(response, dict)
    assert response['id'] == campaign_id


def test_get_deleted():
    response = api.campaigns.get_deleted()
    assert isinstance(response, list)
    assert all(campaign['state'] == 'deleted' for campaign in response)


def test_create():
    name = generate_name(16)
    group_id = 122
    payload = {
        'name': name,
        'group_id': group_id
    }
    response = api.campaigns.create(payload)
    assert isinstance(response, dict)
    assert response['name'] == name
    assert response['group_id'] == group_id


def test_clone():
    name = generate_name()
    group_id = 122
    payload = {
        'name': name,
        'group_id': group_id
    }
    cloning_campaign = api.campaigns.create(payload)

    response = api.campaigns.clone(cloning_campaign['id'])
    assert isinstance(response, list)
    assert response[0]['name'] == 'Copy of ' + cloning_campaign['name']


def test_enable():
    pass


def test_disable():
    pass


def test_restore():
    pass


def test_update():
    pass


def test_move_to_archive():
    pass

test_clone()