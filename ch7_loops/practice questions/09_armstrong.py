#WAP to tell if a number is armstrong or not
#Armstrong number also called a Narcissistic number  example-----153 =1^3 + 5^3 +3^3 = 153   means cubes of all numbers is same as the number

n=int(input("Enter a number: "))
temp=n                          #use temp Because we change the value of n inside the loop. and delete the last digit thats why use temp to save the same number
sum_digits=0

while n>0:
    digit=n%10
    sum_digits +=digit**3                 #make cube of the digit you took out means last digit
    n//=10

if sum_digits==temp:
    print("Armstrong")
else:
    print(" not Armstrong")

