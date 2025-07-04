#f-string

#1st method
name=input("Enter a name: ")
print(name + " Good Afternoon")

#2nd method
a=input("Enter another name: ")
print(f"{a} Good afternoon")             #f string - formatted string literal  
                                         #The f before the string tells Python that it's an f-string. 
                                         # Expressions inside {} are evaluated and replaced with their values.
