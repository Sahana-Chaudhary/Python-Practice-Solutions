'''
--Variable-length arguments--

there is a situation where we need to pass multiple arguments to the function. Such types of arguments are called arbitrary arguments or variable-length arguments.

We use variable-length arguments if we don’t know the number of arguments needed for the function in advance.

Types of Arbitrary Arguments:

1.arbitrary positional arguments (*args)--Think of *args like a bag where you can put as many unnamed values as you want.
Example--
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")

*args packs all extra positional arguments into a tuple.


2.arbitrary keyword arguments (**kwargs)--Use the **kwargs if you want to handle named arguments in a function.
Think of **kwargs like a dictionary for named values.

Example-
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce(name="Alice", age=25, city="London")



The *args and **kwargs allow you to pass multiple positional arguments or keyword arguments to a function.


'''
#Create a function with variable length of arguments
#Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.
# Note: Create this function so that it can receive any number of arguments, process them, and display the value of each individual argument.

def func1(*args):
    for arg in args:
        print(arg)

func1(10,20)
func1("abc","def","ghi")
func1("hello",1,2)
func1()
