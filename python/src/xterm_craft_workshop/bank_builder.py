from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError


class Bankbuilder:
    _exchange_rate: Dict[str, float] = {}

    def __init__(self, exchange_rate = {}) -> None:
        self._exchange_rate = exchange_rate


    def pivotCurrency(currency : Currency):

        pass

    def withExchangeRate(currency: Currency, to: float):
        pass

    def build():
        pass

