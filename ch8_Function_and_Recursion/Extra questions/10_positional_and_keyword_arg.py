'''
When we define and call a Python function, the term parameter and argument is used to pass information to the function.

parameter: It is the variable listed inside the parentheses in the function definition.
argument: It is a value sent to the function when it is called. It is data on which function performs some action and returns the result.


1️⃣ Positional arguments--
The most common way to pass values to a function.
Order matters — the values are matched to parameters in the order they appear.
Only that number of arguments can pass as the parameters entered

Example=
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 25)  # order matches parameters


2️⃣ Keyword arguments

You explicitly name the parameter when passing it.
Order doesn’t matter because the names match directly.
Example--
introduce(age=25, name="Alice")  # order reversed, still works


BOTH
Positional arguments must come first.
Then you can have keyword arguments.

# function with 2 keyword arguments
def student(name, age):
    print('Student Details:', name, age)

# default function call
student('Jessa', 14)

# both keyword arguments
student(name='Jon', age=12)

# 1 positional and 1 keyword
student('Donald', age=13)

'''
#Call Function using both positional and keyword arguments
#Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function using both positional and keyword argument

def describe_pet(animal_type,pet_name):
    print("Animal type: ", animal_type, "Pet name: ", pet_name)

describe_pet("dog","pogo")
describe_pet(pet_name="whiskey", animal_type="cat")

