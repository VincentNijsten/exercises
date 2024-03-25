class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount + other.amount,
                self.currency
            )
        return RuntimeError("Mismathced currencies!")
    
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount - other.amount,
                self.currency
            )
        return RuntimeError("Mismathced currencies!")
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise RuntimeError("Multiplier must be an integer or a float")
        return Money(self.amount * scalar, self.currency)
    


money1 = Money(10, "EUR")
money2 = Money(20, "EUR")

print(money1 + money2)  
print(money2 - money1)  
print(money2 * 5)