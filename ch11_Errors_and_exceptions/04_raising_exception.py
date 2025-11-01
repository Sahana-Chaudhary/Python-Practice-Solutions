#Check age of a person --Use raise for raising exception

def check_age(age):
    if age<=0:
        raise ValueError("Age cant be negative")
    else:
        print("Valid age")

try:
    age=int(input("Enter you age: "))
    check_age(age)
except ValueError as e:
    print("Error: ",e)

    

