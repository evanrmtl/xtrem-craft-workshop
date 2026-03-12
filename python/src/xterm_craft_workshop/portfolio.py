class Portfolio:

    def __init__(self, amount:int=0):
        self.amount = amount
    
    def evaluate(self):
        return self.amount

    def add(self, value:int):
        self.amount += value