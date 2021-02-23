from keitaro.utils import list_to_string, string_to_list


def test_list_to_string():
    ip_list = ['1.2.3.4', '5.3.6.7', '2.1.2.3', '2.7.8.1']
    string_result = list_to_string(ip_list)
    assert isinstance(string_result, str)
    for ip in string_result.split('\n'):
        assert ip in ip_list


def test_string_to_list():
    string_ip_list = '1.2.3.4\n3.4.5.6\n4.5.2.1\n7.8.9.0'
    list_result = string_to_list(string_ip_list)
    assert isinstance(list_result, list)
    for ip in list_result:
        assert ip in string_ip_list.split('\n')
