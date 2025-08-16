#WAP to find whether a given username contains less than 10 characters or not

a=input("enter the username: ")

if(len(a)<10):
    print("less than 10 characters")
else:
    print("more than 10 characters")