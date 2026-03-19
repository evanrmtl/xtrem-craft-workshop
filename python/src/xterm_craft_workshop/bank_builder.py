from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError


class Bankbuilder:
    _exchange_rate: Dict[Currency, (Currency,float)] = []

    def __init__(self, exchange_rate = {}) -> None:
        self._exchange_rate[str(Currency.USD)] = (Currency.USD, 1.2)
        self.pivot_currency = Currency.EUR

    @staticmethod
    def a_bank() -> "Bankbuilder":
        return Bankbuilder()


    def with_pivot_currency(self, currency : Currency):
        self.pivot_currency = currency
        

    def withExchangeRate(self, currency: Currency, to: float):
        self._exchange_rate[str(Currency.USD)] = (Currency.USD, 1.2)
        self._exchange_rate = {currency, to}

    def build(self):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", self._exchange_rate.keys())

        return Bank.create(self.pivot_currency, self._exchange_rate.keys()[0], self._exchange_rate.get(Currency.USD))

