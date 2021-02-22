import json
import random


def test_get(client):
    random_group_type = random.choice(('campaigns', 'offers', 'landings')) 
    resp = client.groups.get(random_group_type)
    assert resp.status_code == 200
    assert resp.json()[0]['type'] == random_group_type