#write a program to print multiplication table of given number using for loop

a=int(input("Enter a number you want table of: "))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

#second method---by using f string

a=int(input("Enter a number you want table of: "))
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")