from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.portfolio import Portfolio

euro = Currency.EUR
usd = Currency.USD
krw = Currency.KRW

class TestPortfolio:
    
    def test_given_empty_portfolio(self):
        #given
        portfolio = Portfolio()

        #when
        result = portfolio.evaluate()

        #then
        assert result == 0

    def test_given_empty_portfolio_when_add_ten_euros(self):
        #given
        portfolio = Portfolio()

        #when
        portfolio.add(10)
        result = portfolio.evaluate()

        #then
        assert result == 10
