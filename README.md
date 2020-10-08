# keitaropy

keitaropy is a simple and easy to use API wrapper library for [Keitaro](https://keitaro.io/) Admin API written in Python3 and [requests](https://pypi.org/project/requests/)

## 📄 Official Keitaro resources

-   [Keitaro Website](https://keitaro.io/)
-   [Admin API documentation](https://admin-api.docs.keitaro.io/)
-   [Technical Support](https://t.me/keitarobot)

## ❔ Why should you use keitaropy

-   allows to use multiple trackers in one solution
-   no need knowledge of http requests
-   incredibly easy to use
-   follows the paradigm "write once, run everywhere"

## 📖 Getting Started

### Installation

To install you need to have [pip](https://pip.pypa.io/en/stable/installing/) installed

```
pip install keitaropy
```

### Keitaro tracker initialization

Begin by importing Keitaro class from keitaropy module and passing Admin API key and URL of Keitaro tracker to it

```python
from keitaropy import Keitaro

api = Keitaro('API key', 'URL')
```

## ⚙ What can it do

All keitaropy functionality is presented in [Google Sheet](https://docs.google.com/spreadsheets/d/1XqRT8XuUG3XfI8GnJMfEKezJmI_3_MllDNermPeUCqA/edit#gid=0)

## 📚 Examples

If API request was successful, status code 200 will be received and a response in the json format. `Use json()` method to see the response data

```python
import json
from keitaropy import Keitaro

api = Keitaro('API key', 'URL')
affnetwork = api.affnetworks.delete(14)
print(affnetwork.json())
```

<details>
  <summary>
    <i>Click to see a response sample</i>
    <a href="https://admin-api.docs.keitaro.io/#tag/Affiliate-Networks/paths/~1affiliate_networks~1{id}/delete">
    Admin API reference</a>
  </summary>
  <p>
    {
      "id": 14,
      "name": "string",
      "postback_url": "string",
      "offer_param": "string",
      "state": "string",
      "template_name": "string",
      "notes": "string",
      "pull_api_options": "string",
      "created_at": "string",
      "updated_at": "string",
      "offers": "string"
    }
  </p>
</details>

### Get all offers or specific one

To get all offers call get() method without any arguments

```python
all_offers = api.offers.get()
```

Let's try to get a specific offer by its id

```python
dummy_offer = api.offers.get(21)
```

As a result you'll get a response in JSON format

<details>
  <summary>
    <i>Click to see a response sample</i>
  </summary>
  <p>
    [
      {
      "id": 21,
      "name": "string",
      "group_id": 0,
      "action_type": "string",
      "action_payload": "string",
      "action_options": [],
      "affiliate_network_id": 0,
      "payout_value": 0,
      "payout_currency": "string",
      "payout_type": "string",
      "state": "string",
      "created_at": {},
      "updated_at": {},
      "payout_auto": true,
      "payout_upsell": true,
      "country": [],
      "notes": "string",
      "affiliate_network": "string",
      "archive": "string",
      "local_path": "string",
      "preview_path": "string"
      }
    ]
  </p>
</details>

### Campaign creation

To create an advertising campaign, you can simply call create() method of the campaigns resource

```python
payload = {
  'name': 'Dummy campaign',
  'state': 'disabled',
  'cost_type': 'CPC',
  'cost_value': '5',
  'cost_currency': 'USD',
  'cost_auto': True
}

campaign = api.campaigns.create(payload)
```
