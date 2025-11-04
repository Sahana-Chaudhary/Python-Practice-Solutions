# Q4. Implement a class BankAccount
# Attributes: account number, name, balance
# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# Add checks for insufficient balance.

class BankAccount():
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposited: ",amount)

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn: ",amount)
    
    def display(self):
        print("Balance left: ",self.balance)

b1=BankAccount(123,"Sahana",1000)
b1.deposit(1000)
b1.display()
b1.withdraw(500)
b1.display()

