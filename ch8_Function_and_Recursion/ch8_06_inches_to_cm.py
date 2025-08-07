#program to convert inches to cm

def inch_to_cm(i):
    return i * 2.54

i=float(input("Enter distance in inches: "))
print(f" Distance in cm: {inch_to_cm(i)} cm")
