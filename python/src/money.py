from dataclasses import dataclass

from .missing_exchange_rate_error import MissingExchangeRateError
from .currency import Currency

@dataclass(init=True, frozen=True, eq=True)
class Money:
    
    amount: float
    currency: Currency

    @staticmethod
    def of(amount: float, currency: Currency) -> "Money":
        return Money(amount, currency)
    
    def __add__(self, other: "Money"):
        if self.currency != other.currency:
            raise ValueError(self.currency, other.currency)
        return Money(self.amount + other.amount, other.currency)
    
    def __mul__(self, other: "Money"):
        if self.currency != other.currency:
            raise ValueError(self.currency, other.currency)
        return Money(self.amount * other.amount, other.currency)
    
def __div__(self, other: "Money"):
        if self.currency != other.currency or other.amount ==0:
            raise ValueError(self.currency, other.currency)
        return Money(self.amount / other.amount, other.currency)