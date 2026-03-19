from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError


class Bankbuilder:
    _exchange_rate: []

    def __init__(self, exchange_rate = {}) -> None:
        self._exchange_rate = {
            str(Currency.USD) : 1.2
        }
        #self._exchange_rate[str(Currency.USD)] = (Currency.USD, 1.2)
        self.pivot_currency = Currency.EUR

    @staticmethod
    def a_bank() -> "Bankbuilder":
        return Bankbuilder()


    def with_pivot_currency(self, currency : Currency)-> "Bankbuilder":
        self.pivot_currency = currency
        return self
        

    def withExchangeRate(self, currency: Currency, to: float) -> "Bankbuilder" :
        self._exchange_rate[str(currency)] = (currency, to)
        return self
    
    def build(self):
        pivot_currency = self.pivot_currency
        from_currency = list(self._exchange_rate.values())[0][0]
        to_currency = list(self._exchange_rate.values())[0][1]
        return Bank.create(pivot_currency, from_currency, to_currency)

