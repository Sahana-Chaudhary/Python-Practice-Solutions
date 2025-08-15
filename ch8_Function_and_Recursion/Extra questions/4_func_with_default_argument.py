'''
What is a default argument?

When you define a function, you can give some parameters a default value.
If the caller doesn’t provide a value for that parameter, Python will use the default.

We assign default values to the argument using the ‘=’ (assignment) operator at the time of function definition. 
You can define a function with any number of default arguments.

Example--
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")   # Pass a value → uses "Alice"
greet()          # No value → uses default "Guest"

It overrides the default value if we provide a value to the default arguments during function calls.


'''

#Create a function with a default argument
#Write a program to create a function show_employee() with the following specifications:
# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000

def show_employee(name,salary=9000):
    print("Name: ",name,"Salary: ", salary)

show_employee("rohan",10000)
show_employee("dipi")

