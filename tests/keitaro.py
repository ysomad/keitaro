import os
import random

from dotenv import load_dotenv

from keitaropy import Keitaro
from keitaropy.models import Model


load_dotenv()
api = Keitaro(os.getenv('API_KEY'), os.getenv('HOST'))


def get_random_id(resources=api.offers.get()):
    return random.randint(1, len(resources))


def generate_name(length=8):
    return 'test_' + Model.generate_alias(length)



