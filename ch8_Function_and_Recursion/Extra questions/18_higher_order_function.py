'''
Higher-order function is a function that does at least one of these two things:

1.Takes another function as an argument
2.Returns a function as its result

Example-
1.Takes another function as an argument
def apply_twice(func, value):
    return func(func(value))

result = apply_twice(lambda x: x + 5, 10)
print(result)  # Output: 20

Here:
apply_twice is higher-order because it accepts func (a function) as an argument.
We pass in lambda x: x + 5 as that function.

2.Returns a function as its result
def multiplier(factor):
    def multiply_by_factor(x):
        return x * factor
    return multiply_by_factor

times3 = multiplier(3)   # returns a new function that multiplies by 3
print(times3(10))        # Output: 30

Here:
multiplier is higher-order because it returns another function.



Built-in Examples of Higher-Order Functions

1.map(function, iterable) — takes a function as an argument.
2.filter(function, iterable) — takes a function as an argument.
3.sorted(iterable, key=function) — takes a function as an argument.
4.functools.partial — returns a new function.
5.decorators — functions that take and return functions.
'''
#Create Higher-Order Function
# Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, and returns the result of calling func(x, y). 
# Demonstrate its use with different functions (e.g., addition, subtraction).
#The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.

def apply_operation(func,x,y):      #higher order function
    return func(x,y)             

def add(a,b):                          # normal function 
    return a+b

subtract = lambda a,b : a-b              #lambda function   can use any of these     


print(apply_operation(add, 10, 5))           
print(apply_operation(subtract, 10, 5))      

