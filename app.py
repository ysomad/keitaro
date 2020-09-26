from keitaropy import Keitaro

import json
import random

import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_KEY')
host = os.getenv('HOST')

api = Keitaro(api_key, host)

# Get all offers
# offers = api.offers.get()
# print(offers)


# Get offer by id
# sbd_test = api.offers.get(870)
# print(sbd_test)


# Create new offer
new_offer = {
    'name': f'test_offer{random.randint(0, 99999)}',
    'affiliate_network_id': 79,
    'action_payload': 'https://cpa.afffarm.com/click?pid=1671&offer_id=58689',
    'payout_currency': 'USD',
    'payout_value': 322,
    'country': 'RU'
}
test_offer = api.offers.create(new_offer)
print(test_offer)


# Clone offer
# cloned_offer = api.offers.clone(880)
# print(cloned_offer)


# Delete offer
# deleted_offer = api.offers.delete(880)
# print(deleted_offer)