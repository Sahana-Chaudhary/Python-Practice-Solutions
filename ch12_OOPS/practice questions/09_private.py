# Q9. Demonstrate Encapsulation
# Create a class Account with:
# Private variable __balance
# Methods deposit(), withdraw(), and get_balance()
# Try accessing __balance directly and see what happens.

class Account():
    def __init__(self):
        self.__balance = 0
    
    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        self.__balance-=amount

    def get_balance(self):
        return self.__balance
    
a1=Account()
a1.deposit(1000)
print(a1.get_balance())
print(a1.__balance)    #gives error brcause its private
