import random

from string import ascii_letters, digits
from urllib.parse import urlparse


def list_to_string(list_items, separator='\n'):
    """
    Converts list items to string with separator
    """
    return separator.join(list_items)


def string_to_list(string, separator='\n'):
    """
    Converts string with separator to a list
    """
    return [word for word in string.split(separator)]


def generate_random_string(length: int = 8) -> str:
    """
    Generates random string of letters and digits with length
    """
    symbols = ascii_letters + digits
    return ''.join(random.choice(symbols) for letter in range(length))


def build_host_url(url: str, scheme: str = 'https') -> str:
    """
    Parses url and adding http scheme if it doesn't exist
    """
    parse_result = urlparse(url, scheme)
    
    if parse_result.netloc:
        netloc = parse_result.netloc
        path = parse_result.path
    else:
        netloc = parse_result.path
        path = ''
    
    host = parse_result._replace(netloc=netloc, path=path)
    return host.geturl()


def remove_key_values(dictionary, keys=['self', '__class__']):
    """
    Removes key values from dictionary
    """
    new_dict = dictionary
    for key in keys:
        del new_dict[key]
    return new_dict


def filter_resource_entities_by_key_value(resource_entities, key, value):
    """
    Filters all resource entities by key and values,
    returns list of resource entities
    """
    found_dicts = [d for d in resource_entities if d[key] == value]
    if not found_dicts:
        raise KeyError(f'resource entities with {key} "{value}" not found')
    return found_dicts


def set_resource_default_fields(args_to_set, query_params, resource_instances):
    for key, value in args_to_set.items():
        if value is None:
            query_params[key] = resource_instances[key]
