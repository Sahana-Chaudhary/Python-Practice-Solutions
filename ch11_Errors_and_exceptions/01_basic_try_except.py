try:
    x=int(input("Enter a number: "))
    print(10/x)

except ZeroDivisionError:
    print("Cant be divided by zero")
except ValueError:
    print("invalid integer")
except Exception as e:
    print("Unexpected error")