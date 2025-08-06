#Recursion---Function that calls itself
'''
factorial(5)=5*4*3*2*1
factorial(4)=4*3*2*1
factorial(1)=1
factorial(0)=1
factorial(n)= n * n-1 * n-2 * ....3 * 2 * 1
factorial(n) = n * factorial(n-1)


'''
def factorial(n):
    if(n==0 or n==1):           #base condition is necessary in recursion
        return 1
    return n * factorial(n-1)      #just because there is return so we have to give a variable to it in main code


n=int(input("Enter a number u want factorial of: "))
print(factorial(n))

