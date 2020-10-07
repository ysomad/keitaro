# keitaropy
keitaropy is a simple and easy to use API wrapper library for [Keitaro](https://keitaro.io/) Admin API written in Python3 and [requests](https://pypi.org/project/requests/)
## 📄 Official Keitaro resources
* [Keitaro Website](https://keitaro.io/)
* [Admin API documentation](https://admin-api.docs.keitaro.io/)

## ❔ Why should you use keitaropy
* allows to use multiple trackers in one solution
* no need knowledge of http requests
* incredibly easy to use

## 📖 Getting Started
### Installation
To install you need to have [pip](https://pip.pypa.io/en/stable/installing/) installed
```
pip install keitaropy
```
### Keitaro tracker initialization
Begin by importing Keitaro class from keitaropy module and passing API key and URL to it
```python
from keitaropy import Keitaro

api = Keitaro('Keitaro Admin API key', 'Keitaro tracker URL')
```

## 📚 Examples
If request is successfully sent, a response will be received. You can see it by simply printing it in console
```python
affnetwork = api.affnetworks.delete(14)
print(affnetwork)
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

### Offers
Let's try to get a specific offer by its id
```python
dummy_offer = api.offers.get(21)
```
As a result you'll get response in JSON format
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

### Campaigns
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


