 #Write a Python script that:
# Prints today’s date in DD-MM-YYYY format
# Asks the user to enter their birthyear 
# Calculates and prints their age in years

import datetime as dt

today=dt.date.today()
print(today.strftime("%d-%m-%Y"))

birth_year=int(input("Enter your birth year: "))
cur_year=dt.date.today().year

age= cur_year-birth_year
print("Your age=",age)



