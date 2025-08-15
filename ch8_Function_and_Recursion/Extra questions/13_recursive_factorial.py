#Write a recursive function to calculate the factorial
#Write a recursive function to calculate the factorial of a non-negative integer.
'''
factorial= n * n-1 * n-2.....3*2*1
factorial = n * factorial(n-1)
# always add base condition in recursion
'''

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(1))