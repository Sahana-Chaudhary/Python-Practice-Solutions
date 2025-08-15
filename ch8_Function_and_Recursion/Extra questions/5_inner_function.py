'''
Inner function---
function defined inside another function.(nested function)

EXample--
def outer():
    print("This is the outer function.")

    def inner():
        print("This is the inner function.")

    inner()  # Calling inner function from inside outer

outer()

'''


#Create an inner function
# Create a program with nested functions to perform an addition calculation as follows:

# Define an outer function that accepts two parameters, a and b.
# Inside this outer function, define an inner function that calculates the sum of a and b.
# The outer function should then add 5 to this sum.
# Finally, the outer function should return the resulting value.”

def outer(a,b):

    def inner_add(a,b):
        return a+b
        
    add=inner_add(a,b)           #calling inner function from outer
    return add+5
    
result=outer(1,2)           #calling outer function
print(result)
