def test_client(api, env_vars):
    assert api.client.api_key == env_vars['api_key']
    assert api.client.host == env_vars['host']
    # TODO: add more tests


def test_env_client(env_api, env_vars):
    assert env_api.client.api_key == env_vars['api_key']
    assert env_api.client.host == env_vars['host']
    # TODO: add more tests
