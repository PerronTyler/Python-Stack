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
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        # your code here
        print(f"Yield Interest:{self.balance * self.int_rate}")
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"Account Balance: {self.account.balance}")
        return self
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(f"Account Balance: {self.account.balance}")
        return self
    def display_user_account_info(self):
        print(f"User Account Balance: {self.account.balance}")
        return self

user_1 = BankAccount(int_rate = 0.01)
print(user_1.balance)

user_2 = BankAccount(int_rate = 0.03,balance = 8000)
print(user_2.balance)

newUser = User("Baby", "baby@gmail.com")
newUser.make_deposit(300)
print(f"New User Deposit: {newUser.account.balance}")
newUser.make_withdraw(100)
print(f"New User Deposit: {newUser.account.balance}")
newUser.display_user_account_info()

# user_1.deposit(300).deposit(300).deposit(300).withdraw(600).yield_interest().display_account_info()
# # # print(user_1.balance)

# user_2.deposit(300).deposit(300).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()
# # print(user_2.balance)