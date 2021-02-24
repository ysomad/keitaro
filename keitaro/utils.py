import random
from string import ascii_letters, digits


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


def remove_class_related_keys_from_local_symbol_table(symbol_table):
    """Removing 'self', '__class__' keys from locals() symbol table"""
    new_symbol_table = symbol_table
    new_symbol_table.pop('self', None)
    new_symbol_table.pop('__class__', None)
    return new_symbol_table


def filter_resource_entities_by_key_value(resource_entities, key, value):
    """Filtering all resource entities by key and values,
    returns list of resource entities"""
    found_dicts = [d for d in resource_entities if d[key] == value]
    if not found_dicts:
        raise KeyError(f'resource entities with {key} "{value}" not found')
    return found_dicts
