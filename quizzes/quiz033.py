# quiz#033

class CompoundInterest:
    def __init__(self, principal:float, rate:float):
        self.principal = principal
        self.rate = rate

    def calculate(self, years:int) -> float:
        return self.principal * (1 + self.rate/100)**years
