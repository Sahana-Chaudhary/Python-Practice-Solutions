#WAP to print sum of digits in number

n=int(input("Enter a number:"))
sum_digits=0

while n>0:
    digit = n%10            #take out the last digit
    sum_digits+= digit     #sum_digit+digit  --add it to sum
    n//=10                  #remove the last digit
print("sum=",sum_digits)
