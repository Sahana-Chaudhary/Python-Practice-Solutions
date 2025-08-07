#convert fahrenheit to celsius

def f_to_c(f):
    return (f - 32) * 5 / 9

f = int(input("Enter temperature in Fahrenheit: "))
print(f_to_c(f))

f = int(input("Enter temperature in Fahrenheit: "))
print(f"{round(f_to_c(f),2)} degree C ")