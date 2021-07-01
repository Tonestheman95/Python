class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = Bankaccount(0,0)
        

    def withdraw(self,amount):
        self.account.withdraw(amount)

    def deposit(self,amount):
        self.account.deposit(amount)
    
    def display_account_info(self):
        self.account.display_account_info(balance)

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


Tonio = User("Tonio Brunetto", "Tonio.Brunetto@Gmail.com")
Tonio.account = Bankaccount(.02,100)
print(Tonio.name)

Tonio.deposit(100)
Tonio.withdraw(50)
#Tonio.display_account_info()
