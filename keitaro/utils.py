import random
from string import ascii_letters, digits

from varname import nameof


def list_to_string(list_items, separator='\n'):
    """Converting list items to string with separator"""
    return separator.join(list_items)


def string_to_list(string, separator='\n'):
    """Converting string with separator to a list"""
    return [word for word in string.split(separator)]


def generate_random_string(length=8):
    """Generating random string of letters and digits with length"""
    symbols = ascii_letters + digits
    return ''.join(random.choice(symbols) for letter in range(length))


def remove_key_values(dictionary, keys=['self', '__class__']):
    """Removing keys values from dictionary"""
    new_dict = dictionary
    for key in keys:
        del new_dict[key]
    return new_dict


def filter_resource_entities_by_key_value(resource_entities, key, value):
    """Filtering all resource entities by key and values,
    returns list of resource entities"""
    found_dicts = [d for d in resource_entities if d[key] == value]
    if not found_dicts:
        raise KeyError(f'resource entities with {key} "{value}" not found')
    return found_dicts


def set_resource_default_fields(args_to_set, query_params, resource_instances):
    for key, value in args_to_set.items():
        if value is None:
            query_params[key] = resource_instances[key]
