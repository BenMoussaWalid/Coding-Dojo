class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -=amount 
            return self
        else :
            print ("Insufficient funds: Charging a $5 fee")
            self.balance-5
            return self
    def display_account_info(self):
        print (self.balance )
        return self 
    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.balance + self.balance*0.01
        return self
user1 = BankAccount(0.01,0)
user2 = BankAccount(0.01,0)
print (user1)
print (user2)
user1.deposit(100).withdraw(50).yield_interest().display_account_info()