from celery import shared_task
from .models import Bitcoin
import requests
import json
from datetime import datetime
from django.utils.timezone import make_aware


@shared_task
def load_btc():
    response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
                            params={'id': 1},
                            headers={'Accept': 'application/json',
                                     'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd'},)

    dict_data = json.loads(response.content)
    price = dict_data["data"]["1"]["quote"]["USD"]["price"]

    datetime_str = dict_data["data"]["1"]["quote"]["USD"]["last_updated"]
    last_updated = make_aware(datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ"))

    info = Bitcoin(price=price, last_updated=last_updated)
    info.save()




