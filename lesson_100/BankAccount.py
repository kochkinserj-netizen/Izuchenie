class BankAccount:

    def __init__(self,amount):
        self.amount = amount

    def __eq__(self, other)-> bool:
        return self.amount == other.amount

    def __add__(self, other):
        return self.amount + other.amount