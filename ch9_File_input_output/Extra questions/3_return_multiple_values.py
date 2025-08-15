#Return multiple values from a function
#Write a function calculation() that accepts two variables and calculates both their addition and subtraction. 
# The function should then return both the sum and the difference in a single return statement.

def calculation(a,b):
    add = a+b
    sub = a-b
    return add,sub

print(calculation(4,5))



