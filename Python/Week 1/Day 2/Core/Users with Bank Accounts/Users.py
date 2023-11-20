class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print(f"nsufficient funds: Charging a $5 fee")
            self.balance - 5
            return self

    def display_account_info(self):
        print("=======================")
        print(self.balance)
        print("=======================")
        return self

    def yield_interest(self):
        self.balance = self.balance + self.balance * 0.01
        return self
#user------------------------------------------------------------------------------------------------
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self


user1 = User("eeee","tft@")
user1 = BankAccount(0.01, 0)
user2 = BankAccount(0.01, 0)
user1.deposit(2000).deposit(1000).deposit(1000).withdraw(1200).yield_interest().display_account_info()
user2.deposit(2000).deposit(1000).deposit(1000).withdraw(1200).yield_interest().display_account_info()