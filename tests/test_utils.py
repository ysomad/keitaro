from keitaro.utils import list_to_string


def test_list_to_string(client):
    ip_list = ['1.2.3.4', '5.3.6.7', '2.1.2.3', '2.7.8.1']
    string_result = list_to_string(ip_list)
    assert isinstance(string_result, str)
    for ip in string_result.split('\n'):
        assert ip in ip_list
