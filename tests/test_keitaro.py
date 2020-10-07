import os
from dotenv import load_dotenv

from keitaropy import Keitaro


def api():
    load_dotenv()
    return Keitaro(os.getenv('API_KEY'), os.getenv('HOST'))