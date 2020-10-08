import os
import random
import json

from dotenv import load_dotenv

from keitaropy import Keitaro
from keitaropy.models import Model


load_dotenv()
api = Keitaro(os.getenv('API_KEY'), os.getenv('HOST'))


def get_random_id(resources):
    return random.choice(resources.json())['id']


def generate_name(test_description, length=8):
    return f'{test_description}_{Model.generate_alias(length)}'



