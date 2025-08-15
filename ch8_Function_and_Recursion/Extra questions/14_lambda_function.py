'''
A lambda function in Python is a small anonymous function defined using the lambda keyword. 
The syntax is lambda arguments: expression. 

arguments → input parameters (like function parameters)
expression → single expression whose result will be returned automatically

The expression is evaluated and returned.

meaning it doesn’t have a formal def name.

It’s written in one line and is often used when you need a short, throwaway function.


'''

#Create a lambda function that squares a given number

square = lambda x: x ** 2
print(square(5))  

'''
This is the same as:

def square(x):
    return x ** 2
'''




