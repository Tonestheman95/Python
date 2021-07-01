from fundamentals.oop.userswithbankaccount import Tonio


class Bankaccount:
    def __init__(self,interest_rate = 0, balance = 0): 
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
            self.balance += amount
            print(self.balance)
            return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("INVALID TRANSACTION")
        elif self.balance > 0:
            self.balance -= amount
            print(self.balance)
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest_Amount = self.interest_rate * self.balance
            self.balance += interest_Amount
        return self


Tonio = Bankaccount(.05,1000)

Tonio.deposit