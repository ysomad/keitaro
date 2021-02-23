import random
from string import ascii_letters, digits


def list_to_string(list_items, separator='\n'):
    return separator.join(list_items)


def string_to_list(string, separator='\n'):
    return [word for word in string.split(separator)]


def generate_random_string(length=8):
    symbols = ascii_letters + digits
    return ''.join(random.choice(symbols) for letter in range(length))


def remove_class_related_keys_from_local_symbol_table(symbol_table):
    new_symbol_table = symbol_table
    symbol_table.pop('self', None)
    symbol_table.pop('__class__', None)
    return new_symbol_table
