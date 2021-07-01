class Bankaccount:
    def __init__(self,interest_rate = 0, balance = 0): 
        self.int_rate = interest_rate
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

    def display_account_info(self, amount):
        print(self.balance)
        return self

    def yield_interest(self, amount):
        if self.balance > 0:
            self.int_rate = amount * self.balance
            print(self.int_rate + self.balance)
        return self

Josh = Bankaccount(0,300)

Josh.deposit (400)
Josh.withdraw(30)
Josh. yield_interest(.05)

Tonio = Bankaccount(0,1000)

Tonio.deposit (200)
Tonio.withdraw(20)
Tonio.yield_interest(.02)