#Create a recursive function
#Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#A recursive function is a function that calls itself repeatedly.
'''
sum = n + n-1 + n-2 ....3+2+1
sum= n+ sum(n-1)

#always add base condition in recursive functions
'''

def sum(n):
    if n==0:
        return 0 
    return n + sum(n-1)

print(sum(10))