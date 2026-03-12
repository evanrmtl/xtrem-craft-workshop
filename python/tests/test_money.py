from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator
from xterm_craft_workshop.money import Money
import pytest


class TestMoney:
    def test_add_in_usd_returns_value(self):
        five_euros = Money.of(5.0, Currency.EUR)
        ten_euros = Money.of(10.0, Currency.EUR)
        fifteen_euros = ten_euros + five_euros

        assert fifteen_euros == Money.of(15, Currency.EUR)

    def test_multiply_in_euros_returns_positive_number(self):
        five_euros = Money.of(5.0, Currency.EUR)
        fifteen_euros = five_euros * 3

        assert fifteen_euros == Money.of(15, Currency.EUR)
    
    def test_different_current_returns_exception(self):
        five_euros = Money.of(5, Currency.EUR)
        three_usd = Money.of(3, Currency.USD)
        with pytest.raises(ValueError):
            a = three_usd + five_euros

    def test_divide_in_usd_and_eur_raise_error(self):
        fifteen_euros = Money.of(15, Currency.EUR)
        assert(fifteen_euros/3 == Money.of(5, Currency.EUR))


    def test_divide_in_eur_returns_float(self):
        fifteen_euros = Money.of(15, Currency.EUR)
        assert(fifteen_euros/3 == Money.of(5, Currency.EUR))

    def test_divide_in_eur_by_zero_raise_error(self):
        fifteen_euros = Money.of(15, Currency.EUR)
        with pytest.raises(ValueError):
            b=fifteen_euros/0