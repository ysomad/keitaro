import os
from dotenv import load_dotenv

from keitaropy import Keitaro


load_dotenv()
api_key = os.getenv('API_KEY')
host = os.getenv('HOST')
api = Keitaro(api_key, host)