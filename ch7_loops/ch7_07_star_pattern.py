#WAP to print star pattern for any value of n
#   *
#  ***
# *****

n=int(input("Enter a value: "))
for i in range (1,n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("\n")

#OR

