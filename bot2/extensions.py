import requests
import json
from config import currencies, TOKEN, API_KEY

class ConvertoinException(Exception):
    pass


class Converter:
    @staticmethod
    def get_convert(quote, base, amount):
        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise APIException(f'Валюта {quote} не найдена!\nСписок доступных валют см. /values')
        try:
            base_ticker = currencies[base]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена!\nСписок доступных валют см. /values')
        if quote_ticker== base_ticker:
            raise APIException(f'Невозможно перевести одинаковые валюты {quote_ticker}')
        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise APIException(f'Неудалось обработать количество: {amount}')

        url = f"https://api.apilayer.com/currency_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"
        payload = {}
        headers = {"apikey": API_KEY}
        r = requests.request("GET", url, headers=headers, data=payload)
        resp = json.loads(r.content)
        print(resp)
        return resp['result']

