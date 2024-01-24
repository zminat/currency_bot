import json
import requests
from config import keys, EXCHANGERATE_TOKEN

class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.\nУвидеть список всех доступных валют: /values')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.\nУвидеть список всех доступных валют: /values')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/{EXCHANGERATE_TOKEN}/pair/{base_ticker}/{quote_ticker}/{amount}')
        total_base = json.loads(r.content)['conversion_result']

        return total_base