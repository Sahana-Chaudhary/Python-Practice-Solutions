#WAP to tell if a number is pandrome or not
# pandrome number is a number whose reverse is also same-can be done for string also

n=int(input("Enter a number: "))
temp=n
rev=0

while n>0:
    d = n%10     #take last digit
    rev = rev*10 +d               #multiplying by 10 shifts the digits one place to the left, so that the new digit can be added to the ones place.
    n//=10                         #remove the number

if(temp==rev):
    print("Palindrome")
else:
    print("Not a palindrome")


