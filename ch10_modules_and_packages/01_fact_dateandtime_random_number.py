#Calculate factorial of number, get current date and time, generate a random number using modules

import math as m
import random as r
import datetime as dt

factorial = m.factorial(5)
print(factorial)

current_datetime=dt.datetime.now()
print(current_datetime)

print(r.randint(1,100)) 