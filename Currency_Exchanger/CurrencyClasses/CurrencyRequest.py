import requests
from .CurrencyAnswer import CurrencyAnswer

class CurrencyRequest():
    def __init__(self, amount, currency_root, currency_target):
        self.amount = round(amount,2)
        self.currency_root = currency_root
        self.currency_target = currency_target

    def fetch_currency_convertion(self):
        """
        Fetch the exchanged amount from https://exchangeratesapi.io/
        :return: CurrencyAnswer object with the result amount and exchange rate
        """
        url = "https://api.exchangeratesapi.io/latest"
        params = {
                  "base": self.currency_root,
                }
        try:
            r = requests.get(url, params=params)
        except:
            print("ERROR -3: Catching the currency - rates failed due to an internet connection error.")
            exit(-3)
        r = r.json()["rates"]
        target_currencies = []
        exchange_rates = []
        #Case 1: Specific target_currencies were given, collect them from the response
        if not self.currency_target == 42:
            target_currencies.append(self.currency_target)
            exchange_rates.append(round(r[self.currency_target],4))
        else:
            target_currencies = list(r.keys())
            exchange_rates = list(r.values())
            exchange_rates = [round(rate,4) for rate in exchange_rates]
        exchange_amounts = [round(rate * self.amount,2) for rate in exchange_rates]

        return CurrencyAnswer(self.currency_root, target_currencies, self.amount, exchange_amounts, exchange_rates)