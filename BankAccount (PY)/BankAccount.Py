from venv import create


class BankAccount:
    # don't forget to add some default values for these parameters!
    balance = 0
    def __init__(self, int_rate, balance=0): 
        # your code here! (remember, instance attributes go here)

        self.int_rate=int_rate
        self.balance=balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        # your code here
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        # your code here
        print(self.balance * self.int_rate)
        return self

user_1 = BankAccount(int_rate = 0.01)
print(user_1.balance)
user_2 = BankAccount(int_rate = 0.03,balance = 8000)
print(user_2.balance)

user_1.deposit(300).deposit(300).deposit(300).withdraw(600).yield_interest().display_account_info()
print(user_1.balance)

user_2.deposit(300).deposit(300).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()
print(user_2.balance)