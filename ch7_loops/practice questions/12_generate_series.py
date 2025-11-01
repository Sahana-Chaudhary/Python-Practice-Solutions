#WAP to generate a series 1,4,9,16,25---n^2

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i**2,end=" ")  