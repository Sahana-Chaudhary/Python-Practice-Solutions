# WAP to find factorial of a given number
#factorial----5!=   1*2*3*4*5

a=int(input("Enter a number: "))
product=1
for i in range(1,a+1):     #to go till that number 
    product = product *  i

print(product)