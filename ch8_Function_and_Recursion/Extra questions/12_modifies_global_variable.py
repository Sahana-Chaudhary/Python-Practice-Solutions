'''
What is a Global Variable?

A global variable is a variable declared outside of all functions in a script.

It can be accessed from anywhere in the program — inside or outside functions.

But modifying it inside a function has some rules.

'''

#Define a global variable global_var = 10. Write a function that modifies a global variable value.

X=20   #global variable

def func():
    global X          # tell Python you mean the global X    #it links x outside function to x inside function so it becomes same
    X = 50
    print("inside function",X)

func()
print("outside func",X)

