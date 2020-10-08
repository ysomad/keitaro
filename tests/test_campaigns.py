from keitaro import api, get_random_id, generate_name


def test_get():
    response = api.campaigns.get()
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, list)


def test_get_by_id():
    campaign_id = get_random_id(api.campaigns.get())
    response = api.campaigns.get(campaign_id)
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, dict)
    assert json['id'] == campaign_id


def test_get_deleted():
    response = api.campaigns.get_deleted()
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, list)
    assert all(campaign['state'] == 'deleted' for campaign in json)


def test_create():
    name = generate_name('test_create')
    group_id = 122
    payload = {
        'name': name,
        'group_id': group_id
    }
    response = api.campaigns.create(payload)
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, dict)
    assert json['name'] == name
    assert json['group_id'] == group_id


def test_clone():
    payload = {
        'name': generate_name('test_clone'),
        'group_id': 122
    }
    cloning_campaign = api.campaigns.create(payload).json()
    response = api.campaigns.clone(cloning_campaign['id'])
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, list)
    assert json[0]['name'] == 'Copy of ' + cloning_campaign['name']


def test_disable():
    payload = {
        'name': generate_name('test_disable'),
        'group_id': 122,
        'state': 'active'
    }
    active_campaign = api.campaigns.create(payload).json()
    response = api.campaigns.disable(active_campaign['id'])
    json = response.json()
    assert response.status_code == 200
    assert json[0]['id'] == active_campaign['id']
    assert json[0]['state'] == 'disabled'


def test_enable():
    payload = {
        'name': generate_name('test_enable'),
        'group_id': 122,
        'state': 'disabled'
    }
    disabled_campaign = api.campaigns.create(payload).json()
    response = api.campaigns.enable(disabled_campaign['id'])
    json = response.json()
    assert response.status_code == 200
    assert json[0]['id'] == disabled_campaign['id']
    assert json[0]['state'] == 'active'


def test_delete():
    payload = {
        'name': generate_name('test_delete'),
        'group_id': 122,
        'state': 'active'
    }
    active_campaign = api.campaigns.create(payload).json()
    response = api.campaigns.delete(active_campaign['id'])
    json = response.json()
    assert response.status_code == 200
    assert json[0]['id'] == active_campaign['id']
    assert json[0]['state'] == 'deleted'


def test_restore():
    payload = {
        'name': generate_name('test_restore'),
        'group_id': 122,
        'state': 'deleted'
    }
    deleted_campaign = api.campaigns.create(payload).json()
    response = api.campaigns.restore(deleted_campaign['id'])
    json = response.json()
    assert response.status_code == 200
    assert json[0]['id'] == deleted_campaign['id']
    assert json[0]['state'] == 'active'


def test_update():
    name = generate_name('test_update')
    payload = {
        'name': name,
        'group_id': 122,
    }
    campaign = api.campaigns.create(payload).json()
    updated_name = name + '_updated'
    update_payload = {
        'group_id': 122,
        'name': updated_name,
        'cost_value': '11',
        'cost_auto': False,
        'traffic_source_id': 3
    }
    response = api.campaigns.update(campaign['id'], update_payload)
    json = response.json()
    assert response.status_code == 200
    assert json['name'] == updated_name
    assert json['id'] == campaign['id']
    assert json['cost_value'] == '11'
    assert json['cost_auto'] == False