#function is group of statements performing a specific task
# it can be reused in a task


#Function Definition
def avg():
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c=int(input("Enter the number: "))
    average=(a+b+c)/3
    print(average)

#calling a function--Function call
avg()              #main code--main code runs first  

#quick quiz
def greet():
    print("Good Day! " + name)

name=input("Enter your name-")
greet()

#Types of functions
#1. Built-in functions   -already present in python
#2. User defined functions   -user defines them

#Function with argument
def greet(name,ending):
    print("Good Day! " + name + ending)

greet("sahana"," thankyou")  #we have given both arguments so it works otherwise it will show error
greet("abc"," t")

# if we put it in a variable or something we have to put return in function to return a value in output
def greet(name,ending):
    print("Good Day! " + name + ending)
    return "done"

d = greet("sahana"," thankyou")    
print(d)

#can do like this also
def greet(name,ending="Thankyou"):   # like this it will now show error because we have specified in function
    print("Good Day! " + name )
    print(ending)

greet("Harry")





