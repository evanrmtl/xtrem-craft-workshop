import pytest

from src.currency import Currency
from src.money import Money

from src.money_calculator import MoneyCalculator

class TestMoney:
    def test_add_in_usd_returns_value(self):
        five_euros = Money.of(5.0, Currency.EUR)
        ten_euros = Money.of(10.0, Currency.EUR)
        fifteen_euros = ten_euros + five_euros

        assert fifteen_euros == Money.of(15, Currency.EUR)

    def test_multiply_in_euros_returns_positive_number(self):
        five_euros = Money.of(5.0, Currency.EUR)
        three_euros = Money.of(3.0, Currency.EUR)
        fifteen_euros = five_euros * three_euros

        assert fifteen_euros == Money.of(15, Currency.EUR)
    
    def test_different_current_returns_exception(self):
        five_euros = Money.of(5, Currency.EUR)
        three_usd = Money.of(3, Currency.USD)
        with pytest.raises(ValueError):
            a = three_usd + five_euros

    def test_divide_in_usd_and_eur_raise_error(self):
        fifteen_euros = Money.of(15, Currency.EUR)
        three_usd = Money.of(3, Currency.USD)
        with pytest.raises(ValueError):
            b=fifteen_euros/three_usd


    def test_divide_in_eur_returns_float(self):
        fifteen_euros = Money.of(15, Currency.EUR)
        three_euros = Money.of(3, Currency.EUR)
        assert(fifteen_euros/three_euros==5)

    def test_divide_in_eur_by_zero_raise_error(self):
        fifteen_euros = Money.of(15, Currency.EUR)
        zero_euro = Money.of(0, Currency.EUR)
        with pytest.raises(ValueError):
            b=fifteen_euros/zero_euro