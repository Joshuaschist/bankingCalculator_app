from .exceptions import LowBalanceError

class Account:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("Deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise LowBalanceError("Not enough balance")
        self.balance -= amount
        self.history.append(("Withdraw", amount))

    def get_balance(self):
        return self.balance

    def transactions(self):
        for t in self.history:
            yield t