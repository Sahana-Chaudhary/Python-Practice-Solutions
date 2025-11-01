try:
    a=int(input("Enter a number: "))
    result=a/100
except ZeroDivisionError:
    print("cant be 0")
    
else:                                     #if except does not work then else
    print("Result: ",result)
finally:                                    #will implement no matter what
    print("Operation complete")